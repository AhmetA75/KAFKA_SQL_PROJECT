from kafka import KafkaAdminClient, KafkaConsumer
import json
import psycopg2

	
ORDER_KAFKA_CONFIRMED_TOPIC="order_confirmed"             # This is the topic name
	
consumer=KafkaConsumer(
	    ORDER_KAFKA_CONFIRMED_TOPIC,
	    bootstrap_servers="localhost:9092"
	)
	
email_sent_so_far=set()
print("Email is listening")

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5434")     # Connect to the database
cur = conn.cursor()

for message in consumer:
    consumed_message=json.loads(message.value.decode())
    customer_email=consumed_message["customer_email"]
    
    cur.execute("INSERT INTO email (email) VALUES (%s)" ,(customer_email,))                                 # Insert the data into the database
    
    conn.commit()
    print(f"Sending email to {customer_email}")
    email_sent_so_far.add(customer_email)
    print(f"So far emails sent to :{len(email_sent_so_far)} unique emails")                   # Print the number of unique emails

conn.close()           # Close the connection

# Please Read
# After created tables and composed the docker-compose.yml file, you can run this code as first step:
# You need to run the following command in the terminal: python3.10.exe .\email_send.py 
# In this step, i send the data from kafka to postgresql  "email" database.