import pika # RabbitMQ

params = pika.URLParameters('amqps://ykaotyzw:Jnxjf90ng-3yBPYp9uCx6N5zED0R6Ifq@seal.lmq.cloudamqp.com/ykaotyzw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()