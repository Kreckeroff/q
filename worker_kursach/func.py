from .models import *
import sqlite3
from django.db import connection

def addConf(Title, ConfDate, ConfTag):
    connection = sqlite3.connect("db.sqlite3")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('INSERT INTO worker_kursach_conference ("Title","ConfDate","ConfTag") VALUES (?,?,?)'
                 ' RETURNING *', (Title, ConfDate, ConfTag))
    row = cursor.fetchone()
    cursor.close()
    connection.commit()
    return dict(row)

def getConf(Title, ConfDate, ConfTag):
    connection = sqlite3.connect("db.sqlite3")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(
        '''SELECT * FROM worker_kursach_conference WHERE "Title" LIKE ? AND "ConfDate" LIKE ? AND "ConfTag" LIKE ? ''', (f"%{Title}%", f"%{ConfDate}%", f"%{ConfTag}%"))
    row = cursor.fetchall()
    cursor.close()
    connection.commit()
    row = [dict(i) for i in row]
    print(row)
    return row