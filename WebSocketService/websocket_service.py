import asyncio
import websockets
import json
import jwt
from datetime import datetime, timedelta
import httpx
from config import settings

active_users = {}
session_expiry = {}

def verify_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        raise Exception("Token expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")

async def handler(websocket, path):
    try:
        token = await websocket.recv()
        user_id = verify_token(token)

        active_users[user_id] = websocket
        session_expiry[user_id] = datetime.utcnow() + timedelta(seconds=settings.SESSION_TIMEOUT)
        print(f"User {user_id} connected.")

        while True:
            message = await websocket.recv()
            print(f"Received message from {user_id}: {message}")

            if datetime.utcnow() > session_expiry[user_id]:
                await websocket.send(json.dumps({"error": "Session expired"}))
                break

            session_expiry[user_id] = datetime.utcnow() + timedelta(seconds=settings.SESSION_TIMEOUT)

            response = {
                "message": "Message received",
                "user_id": user_id,
                "timestamp": str(datetime.utcnow())
            }
            await websocket.send(json.dumps(response))

    except websockets.exceptions.ConnectionClosed:
        print(f"User {user_id} disconnected.")
        active_users.pop(user_id, None)
        session_expiry.pop(user_id, None)

async def create_channel(user_id):
    if user_id not in active_users:
        raise Exception(f"User {user_id} is not connected.")
    websocket = active_users[user_id]
    response = {"message": "Channel created successfully", "timestamp": str(datetime.utcnow())}
    await websocket.send(json.dumps(response))

async def notify_websocket_service(access_token):
    url = "ws://localhost:8765"
    async with websockets.connect(url) as websocket:
        await websocket.send(access_token)
        response = await websocket.recv()
        print(f"WebSocket response: {response}")

async def session_monitor():
    while True:
        now = datetime.utcnow()
        expired_users = [user_id for user_id, expiry in session_expiry.items() if now > expiry]
        for user_id in expired_users:
            print(f"Session expired for user {user_id}. Disconnecting.")
            websocket = active_users.pop(user_id, None)
            session_expiry.pop(user_id, None)
            if websocket:
                await websocket.close()
        await asyncio.sleep(10)

async def main():
    server = await websockets.serve(handler, "0.0.0.0", 8765)
    print("WebSocket server started on ws://0.0.0.0:8765")

    await asyncio.gather(server.wait_closed(), session_monitor())

if __name__ == "__main__":
    asyncio.run(main())
