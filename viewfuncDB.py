import sqlite3
import os

from flask import Flask, request
from random import choice
from string import ascii_lowercase, digits

app = Flask('app')

@app.route('/gen_password')
def gen_password():
	badges = ascii_lowercase
	dig = int(request.args.get('dig'))
	if dig == None:
		badges 
	else:
		badges += digits
	
	length = int(request.args.get('length', 10))
	if (8 <= length <= 24):
		return ''.join([choice(badges) for _ in range(length)])
	else:
		return 'Please specify the length in the range from 8 to 24'


@app.route('/filter_by_state_city')
def filter_by_state_city():
    query = 'SELECT State, City FROM Customers'
    return f'{execute_query(query)}'

@app.route('/counting_unique_firstnames')
def counting_unique_firstnames():
    query = 'SELECT DISTINCT FirstName FROM Customers'
    return len(execute_query(query))
	# query = 'SELECT COUNT(DISTINCT FirstName) FROM Customers'  # ??
	# return execute_query(query)


@app.route('/get_turnover')
def get_turnover():
    query = 'SELECT SUM(UnitPrice*Quantity) FROM invoice_items'
    return f'{execute_query(query)[0][0]}'


def execute_query(query):
    db_path = os.path.join(os.getcwd(), 'chinook.db')  # создание пути
    connection = sqlite3.connect(db_path)  # создание объекта подключения
    curs = connection.cursor()  # создание объекта курсора
    curs.execute(query)  # создание таблицы
    return curs.fetchall()  # получение результатов

app.run()
