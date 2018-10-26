import pika
import requests
import json
import time 


content=dict(wsdir='some',host='thing',reviewid='dummy')

wsdir=content['wsdir']
host=content['host']
reviewid=content['reviewid']

# Publish to RabbitMQ
###############################################################################
print("Connecting to RabbitMQ broker")
start=time.time()
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='test')
#default empty exchange with routing key equal to the queue name 

data={"wsdir":str(wsdir),"host":str(host),"reviewid":str(reviewid)}

#will route the message to that queue
channel.basic_publish(exchange='',routing_key='test',body=json.dumps(data))
print("Published to Queue!"+str(reviewid))

connection.close()
elapsed = time.time() - start
print("Publishing time:",elapsed)
###############################################################################