import psycopg2
conn = psycopg2.connect(database='flask_db', host='localhost', user='postgres', password='kaushik', port='5432')
curr = conn.cursor()
curr.execute('''CREATE TABLE IF NOT EXISTS courses (id serial PRIMARY KEY , name varchar(255) NOT NULL, fess integer, duration integer);''')
curr.execute('''INSERT INTO courses (name, fess, duration) VALUES ('Python', 6000, 45), ('JAVA', 6400, 50);''')
conn.commit()
curr.close()
conn.close()
