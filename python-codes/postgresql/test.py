# coding=utf-8

import psycopg2

conn = psycopg2.connect("dbname=test user=testuser password=7104carl")
cur = conn.cursor()

#cur.execute("CREATE TABLE FilesList (ID serial PRIMARY KEY, FilePath varchar, FileStat integer);")

#cur.execute("INSERT INTO FilesList (FilePath, FileStat) VALUES (%s, %s)", ("d:/a/b", 2))

cur.execute("SELECT * FROM FilesList;")
cur.fetchone()

conn.commit()
cur.close()
conn.close()