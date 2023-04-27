import os
import psycopg2

conn = psycopg2.connect(
    database=os.environ.get('DB_NAME'),
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    port=os.environ.get('DB_PORT')
  )

cursor = conn.cursor()

cursor.execute("""
  SELECT * FROM users;
""")

result = cursor.fetchall();

for data in result:
    print(data)

cursor.close()

conn.commit()

print('deu certo!')