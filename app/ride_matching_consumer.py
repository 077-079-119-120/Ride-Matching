# Code for Ride Matching Consumer
import os 
import requests
import pika
import time

server_ip = os.getenv('SERVER_IP',"localhost")
consumer_id = os.getenv('CONSUMER_ID',"default")
r= requests.post(server_ip,json={"consumer_id":cosumer_id})#Format string server ip to localhost:

channel.queue_declare(queue='ride-share')

def callback(ch,method,properties,body):
	sleep_time = int(body)
	time.sleep(sleep_time)
	print(consumer_id)#Also print task id ?
channel.basic_consume(queue='ride_share',auto_ack=True,on_message_callback=callback)



