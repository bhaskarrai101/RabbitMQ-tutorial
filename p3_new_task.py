import sys
import pika

# define connection and host or ip address
credentials = pika.PlainCredentials('admin','admin')


connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1',5672,'/',credentials))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ''.join(sys.argv[1:]) or "Hello World!"

#channel.basic_publish(exchange='',
#                      routing_key='hello',
#                      body='Hello World!')
#print("[x] Sent 'Hello world!'")



channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,)
                      #properties=pika.BasicProperties(delivery_mode=2,))

print(" [x] Sent %r" % message )

connection.close()



