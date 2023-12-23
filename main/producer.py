import pika, json

params = pika.URLParameters('amqps://ykaotyzw:Jnxjf90ng-3yBPYp9uCx6N5zED0R6Ifq@seal.lmq.cloudamqp.com/ykaotyzw')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)