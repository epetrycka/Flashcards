import aio_pika
import os

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost/")

async def publish_event(event_type: str, payload: dict):
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        exchange = await channel.declare_exchange("user.events", aio_pika.ExchangeType.TOPIC)
        await exchange.publish(
            aio_pika.Message(body=str(payload).encode()),
            routing_key=event_type
        )
