from ensurepip import bootstrap
import imp
import json	
from kafka import KafkaConsumer
from kafka import KafkaProducer
from faker import Faker

fake = Faker()
num= fake.iana_id()
numm= fake.iana_id()
	
ORDER_KAFKA_TOPIC="order_details"                                # This is the topic name
ORDER_CONFIRMED_KAFKA_TOPIC="order_confirmed"                     
	
	
consumer=KafkaConsumer(
	    ORDER_KAFKA_TOPIC,
	    bootstrap_servers="localhost:9092"
	)
producer=KafkaProducer(
bootstrap_servers="localhost:9092")                             
	
print("Gonna start listening")

total_order_counts = 0
total_revenue = 0
	    
for message in consumer:                                        # This is the loop for listening the data from kafka
	print("Updating analytics")
	consumed_message=json.loads(message.value.decode())
	
	user_id=consumed_message["user_id"]
	urun_count=consumed_message["urun_count"]
	urun_deger=consumed_message["urun_deger"]
	total_cost = urun_count * urun_deger
	order_id=consumed_message["order_id"]

	data={
				"customer_id":user_id,
				"customer_email": f'{user_id}@gmail.com',             # This is the email address created by using the user_id
				"total_cost":total_cost,
				"order_id":order_id
				 
	}
	print("Successful Transactions...")
	producer.send(ORDER_CONFIRMED_KAFKA_TOPIC, value=json.dumps(data).encode("utf-8"))          # This is the code for sending the data to the kafka topic
	producer.flush()


total_cost=float(consumed_message["total_cost"])
total_order_counts+=1
total_revenue+=total_cost  

print(f"Orders so far today : {total_order_counts}")
print(f"Total revenue so far today : {total_revenue}")




# This is your third step to run the code please run the following command in the terminal: python3.10.exe .\order_backend.py
# In this third i read datas coming from order_badckend and created an email belongs to the user id and i sent
# datas to listening queue.