from kafka import KafkaAdminClient, KafkaConsumer
import json
import psycopg2

	
ORDER_KAFKA_CONFIRMED_TOPIC="order_confirmed"
	
consumer=KafkaConsumer(
	    ORDER_KAFKA_CONFIRMED_TOPIC,
	    bootstrap_servers="localhost:9092"
	)
	
email_sent_so_far=set()
print("Listening post is listening")

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5434")  # Connect to the database
cur = conn.cursor()    # Create a cursor object


for message in consumer:                                      # For each message in the consumer      
	consumed_message=json.loads(message.value.decode())
	#customer_email=consumed_message["customer_email"]
	customer_id=consumed_message["customer_id"]
	total_cost=consumed_message["total_cost"]
	order_id=consumed_message["order_id"]

	# conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5434")
	# cur = conn.cursor()

	cur.execute("INSERT INTO orders (id,order_id,cost) VALUES (%s, %s, %s)", (customer_id, order_id, total_cost))   # Insert the data into the database
	#cur.execute("INSERT INTO email (email) VALUES (%s)", (customer_email))
	conn.commit()

	print(f"Sending email to {customer_id}")
	#email_sent_so_far.add(customer_email)
	print(f"So far emails sent to :{len(email_sent_so_far)} unique emails")

conn.close()

# This is your second step: for running the kafka and python code, you need to run the following command in the terminal: python3.10.exe .\listening_post.py
# In this step, i send the data from kafka to postgresql  "orders" database.


