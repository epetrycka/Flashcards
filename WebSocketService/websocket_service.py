import asyncio
import websockets
import json
from datetime import datetime

def verify_token(token):
    # weryfikujesz token, np. używasz biblioteki `jwt` do dekodowania tokenu
    # UserService, aby potwierdzić tożsamość.
    return "user_123"

async def handler(websocket, path):
    try:
        token = await websocket.recv()
        user_id = verify_token(token)
        print(f"User {user_id} connected.")
        
        while True:
            data = await websocket.recv()
            print(f"Received message from user {user_id}: {data}")
            
            response = {"message": f"Hello, user {user_id}", "data": data, "timestamp": str(datetime.utcnow())}
            await websocket.send(json.dumps(response))
    
    except websockets.exceptions.ConnectionClosed:
        print(f"User disconnected.")

async def main():
    server = await websockets.serve(handler, "0.0.0.0", 8765)
    print(f"WebSocket server started on ws://0.0.0.0:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
