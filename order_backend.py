from ensurepip import bootstrap
import random
import time 
import json
from faker import Faker

fake = Faker()                                      # This is the faker library to generate fake data.
	
from kafka import KafkaProducer                     # This is the kafka library to send data to kafka.
	
ORDER_KAFKA_TOPIC="order_details"                  # This is the topic name
ORDER_LIMIT = 20000                                # This is the limit of the orders
	
producer=KafkaProducer(bootstrap_servers="localhost:9092")
	
print("Going to be generating order after 10 seconds")
print("will generate one unique order after every 10 seconds")

offset = 150	
	
for i in range(offset, offset + ORDER_LIMIT):
	
	user_id = fake.unique.first_name()             #Creating a unique user_id via faker
	order_id = (fake.iana_id())                    #Creating a unique order_id via faker
	#email = f'{user_id}@gmail.com'
	urun_count = random.randint(1, 10)             #Creating a random number between 1 and 10
	urun_deger = random.randint(50, 100)           #Creating a random number between 50 and 100
	
	data={
	        "order_id":order_id,                 #Creating a dictionary
	        "user_id":user_id,                   
			#"email":email,
	        "urun_count":urun_count,
	        "urun_deger":urun_deger
	    }
	try:                                               #This is the try and except block to handle the errors.

		producer.send(ORDER_KAFKA_TOPIC, value=json.dumps(data).encode("utf-8"))           #Sending the data to the kafka topic
		producer.flush()
	except Exception as err:
		print(err)
	
print(f"Done sending...{i}")
	    # time.sleep(3)




# This is your fourth step to run the code please run the following command in the terminal: python3.10.exe .\order_generator.py

# Last Words all these codes must run in order for preventing errors.

# In this project i created sql tables for sending data to the database and i used docker and kafka queues for sending data to the database.
# About datas i used faker library for generating fake datas.
# for the integers i used random library.