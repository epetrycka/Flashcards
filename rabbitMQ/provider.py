import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange = '',
                      routing_key = 'hello',
                      body = 'My message hello world')
print(" [x] Sent message")

connection.close()