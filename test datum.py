import psycopg2
import time

start_time = time.perf_counter()



hostname = 'localhost'
database = 'OLC Test'
username = 'postgres'
pwd = 'Akbulut23'
port_id = 5432

conn = None
cur = None

try:
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)
    print('DataBase connected')


    cur = conn.cursor()


    query = "INSERT INTO leerlingen (id, naam, email, boek, auteur) VALUES (%s,%s,%s,%s,%s)"
    with open("OLCtest_tabletext") as f:
        f_record = f.readlines()
        values = [line.strip().split(' , ') for line in f_record]
        cur.executemany(query, values)
    # commit the changes
    conn.commit()
    count = cur.rowcount
    print(count, "Record inserted successfully into table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert File into table", error)


finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()



"""
    cur.execute("insert into leerlingen")

    cur.execute("select id, naam from leerlingen")

    rows = cur.fetchall()

    for r in rows:
        print(f"id {r[0]} naam {r[1]}")
"""