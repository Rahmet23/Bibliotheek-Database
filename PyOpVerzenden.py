import psycopg2
import time

start_time = time.perf_counter()



hostname = 'localhost'
database = 'OLC SchoolBieb'
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


    query = "INSERT INTO boek (boeknr, titel, auteur, uitgever, isbn) VALUES (%s,%s,%s,%s,%s)"
    with open("boek_tabletext") as f:
        f_record = f.readlines()
        values = [line.strip().split(' , ') for line in f_record]
        cur.executemany(query, values)
    # commit the changes
    conn.commit()
    count = cur.rowcount
    print(count, "Record boek inserted successfully into table")

    query2 = "INSERT INTO exemplaar (exemplaarnr, boeknr) VALUES (%s,%s)"
    with open("exemplaar_tabletext") as f:
        f_record2 = f.readlines()
        values2 = [line.strip().split(' , ') for line in f_record2]
        cur.executemany(query2, values2)
    conn.commit()
    count2 = cur.rowcount
    print(count2, "Record exemplaar is succesfully inserted into table")

    query3 = "INSERT INTO leerling (leerlingnr, naam, adres, woonplaats) VALUES (%s,%s,%s,%s)"
    with open("leerling_tabletext") as f:
        f_record3 = f.readlines()
        values3 = [line.strip().split(' , ') for line in f_record3]
        cur.executemany(query3, values3)
    conn.commit()
    count3 = cur.rowcount
    print(count3, "Record leerling is succesfully inserted into table")

    query4 ="INSERT INTO reservering (leerlingnr, boeknr, reserveringsdatum) VALUES (%s,%s,%s)"
    with open("reservering_tabletext") as f:
        f_record4 = f.readlines()
        values4 = [line.strip().split(' , ') for line in f_record4]
        cur.executemany(query4, values4)
    conn.commit()
    count4 = cur.rowcount
    print(count4, "Record reservering is succesfully inserted into table")

    query5 ="INSERT INTO uitleningen (uitleningnr, leerlingnr, exemplaarnr, begindatum, einddatum) VALUES (%s,%s,%s,%s,%s)"
    with open("uitlening_tabletext") as f:
        f_record5 = f.readlines()
        values5 = [line.strip().split(' , ') for line in f_record5]
        cur.executemany(query5, values5)
    conn.commit()
    count5 = cur.rowcount
    print(count5, "Record uitlening is succesfully inserted into table")


except (Exception, psycopg2.Error) as error:
    print("Failed to insert File into table", error)


finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()