# Code for Producer
from flask import Flask
import pika

app = Flask(__name__)
mapping = dict() 
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='ride-sharing')
channel.queue_declare(queue='database')

@app.route('/new_ride',methods=['POST'])
def get_data():
	if request.method=='POST':
		pickup = request.form.get('pickup')
		destination = request.form.get('destination')
		time = request.form.get('time')
		cost= request.form.get('cost')
		seats= request.form.get('seats')
		#put these in the database queue
	
@app.route('/new_ride_matching_consumer',methods=['POST'])
def map():
	if request.method=='POST':
		ip = request.remote_addr
		consumer_id = request.form.get('consumer_id')
		mapping['Name']=consumer_id
		mapping['ip']=ip
		#put these in the ride_sharing queue






		
		
