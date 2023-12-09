import pika # RabbitMQ

params = pika.URLParameters('amqps://ykaotyzw:Jnxjf90ng-3yBPYp9uCx6N5zED0R6Ifq@seal.lmq.cloudamqp.com/ykaotyzw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')