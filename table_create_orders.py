import psycopg2

sql_query = "CREATE TABLE orders(id VARCHAR, order_id VARCHAR,cost VARCHAR);"           # Create the "orders" table in the database



conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5434")          # Connect to the database
cur = conn.cursor()

cur.execute(sql_query)
conn.commit()

conn.close()


# Use this code to create the  "orders" table in the  database via psycopg2 before kafka and python code