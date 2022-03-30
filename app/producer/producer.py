# Code for Producer
from flask import Flask,request
import os 
import pika
import json
import time 
time.sleep(15)
app = Flask(__name__)
map_array = list() 
amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(url_params)

channel = connection.channel()
channel.queue_declare(queue='ride-sharing')
channel.queue_declare(queue='database')
port = 5200

@app.route('/new_ride',methods=['POST'])
def get_data():
	data_dict = dict()
	if request.method=='POST':
		pickup = request.args.get('pickup')
		destination = request.args.get('destination')
		ride_time = request.args.get('time')
		str_time = str(ride_time)
		cost= request.args.get('cost')
		seats= request.args.get('seats')
		data_dict = {'pickup':pickup,'destination':destination,'time':ride_time,'cost':cost,'seats':seats}
		data_json=json.dumps(data_dict)
		channel.basic_publish(exchange='',routing_key='ride-sharing',body=str_time)
		print(str_time,"put on ride_sharing queue")
		channel.basic_publish(exchange='',routing_key='database',body=data_json)
		return "Done"
			
@app.route('/new_ride_matching_consumer',methods=['POST'])
def map():
	mapping = dict()
	if request.method=='POST':
		ip = request.remote_addr
		consumer_id = request.form.get('consumer_id')
		mapping['Name']=consumer_id
		mapping['ip']=ip
		map_array.append(mapping)
		return "done"



if __name__ == "__main__":
	print('Producer started')
	app.run(host="0.0.0.0",port=port)
	


		
		
