# Code for Producer
from flask import Flask
import pika
import json

app = Flask(__name__)
map_array = list() 
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='ride-sharing')
channel.queue_declare(queue='database')

@app.route('/new_ride',methods=['POST'])
def get_data():
	data_dict = dict()
	if request.method=='POST':
		pickup = request.form.get('pickup')
		destination = request.form.get('destination')
		time = request.form.get('time')
		str_time = str(time)
		cost= request.form.get('cost')
		seats= request.form.get('seats')
		data_dict = {'pickup':pickup,'destination':destination,'time':time,'cost':cost,'seats':seats}
		data_json=json.dumps(data_dict)
		channel.basic_publish(exchange='',routing_key='ride-sharing',body=str_time)
		print(str_time,"put on ride_sharing queue")
		channel.basic_publish(exchange='',routing_key='database',body=data_json)
		
			
@app.route('/new_ride_matching_consumer',methods=['POST'])
def map():
	mapping = dict()
	if request.method=='POST':
		ip = request.remote_addr
		consumer_id = request.form.get('consumer_id')
		mapping['Name']=consumer_id
		mapping['ip']=ip
		map_array.append(mapping)






		
		
