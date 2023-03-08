import psycopg2 as pg2

conn = pg2.connect(dbname="dvdrental", user="postgres", password="8988")

cur = conn.cursor()

query = "select * from payment;"

cur.execute(query)

# all_records = cur.fetchall()
# print(all_records)

# some_records = cur.fetchmany(5)
# print(some_records)

record = cur.fetchone()
print(record)

# conn.close()
