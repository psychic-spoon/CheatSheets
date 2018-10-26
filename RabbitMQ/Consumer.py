import pika
import requests
import json
import time

# defining the api-endpoint 
API_ENDPOINT = "http://0.0.0.0:5027/myjob"

def handler(ch, method, properties, body):
    print("-> Handled: [%s]" % (body))
    #Extract data from body and call the job and wait for response
    #API endpoint should be updating database
    # sending post request and saving response as response object
    #Extract data from body
    
    datastore = json.loads(body.decode('utf-8'))
    
    wsdir=datastore['wsdir'] 
    host=datastore['host']
    reviewid=datastore['reviewid']

    data={"wsdir":str(wsdir),"host":str(host),"reviewid":str(reviewid)}    
    print(data)
    print("Posting data to myJob")

    r = requests.post(url = API_ENDPOINT, data = json.dumps(data))    
    
    time.sleep(5)

    ch.basic_ack(delivery_tag = method.delivery_tag)
    print("Dequing the queue now")




connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

print('Consumer started. Handling queue messages.')

channel.basic_consume(handler, queue='test', no_ack=False)
channel.start_consuming()