import psycopg2

sql_query = "CREATE TABLE email(email VARCHAR);"                  # Create the "email" table in the database
conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5434")                 # Connect to the database
cur = conn.cursor()

cur.execute(sql_query)     # Execute the query
conn.commit()

conn.close()              # Close the connection

# Use this code to create the "email" table in the database via psycopg2 before kafka and python code