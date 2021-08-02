import time
import pika



credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1',5672,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for message. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    #ch.basic_ack(delivery_tag=method.delivery_tag)
    

#channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message_callback=callback, queue='task_queue', auto_ack=True)


#print('[*] Waiting for message')

channel.start_consuming()
    

















