import psycopg2
import os


DATABASE_URL = os.environ['DATABASE_URL']


def addtodb(content):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    sql = "INSERT INTO STUDENT (NAME) VALUES (%s)"
    a = (content,)
    cursor.execute(sql, a)
    conn.commit()
    conn.close()
