# Code for Ride Matching Consumer
import os 
import requests
import pika
import time

time.sleep(15)
amqp_url = os.environ['AMQP_URL']
server_url = os.environ['SERVER_URL']
consumer_id = os.environ['CONSUMER_ID']
url_params = pika.URLParameters(amqp_url)


consumer_id = os.getenv('CONSUMER_ID',"default")
send_to = server_url
r= requests.post(send_to,json={"consumer_id":consumer_id})#Format string server ip to localhost: 
connection = pika.BlockingConnection(url_params)
channel = connection.channel()
channel.queue_declare(queue='ride-sharing')

def callback(ch,method,properties,body):
	sleep_time = int(body)
	print(sleep_time)
	time.sleep(sleep_time)
	print(consumer_id)#Also print task id ?

channel.basic_consume(queue='ride-sharing',auto_ack=True,on_message_callback=callback)
#connection.close()
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

