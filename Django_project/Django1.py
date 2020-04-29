import sqlite3
import os
import json

from random import choice
from string import ascii_lowercase, digits
from django.shortcuts import render
from django.http import HttpResponse


def gen_password(request):
	badges = ascii_lowercase
	dig = int(request.GET.get('dig'))
	if dig == None:
		badges
	else:
		badges += digits

	length = int(request.GET.get('length', 10))
	if (8 <= length <= 24):
		return HttpResponse(''.join([choice(badges) 
							for _ in range(length)]))
	else:
		return HttpResponse('Please specify the length \
							in the range from 8 to 24')


def filter_by_state_city(request):
	query = 'SELECT State, City FROM Customers'
	return HttpResponse(f'{execute_query(query)}')


def counting_unique_firstnames(request):
	query = 'SELECT DISTINCT FirstName FROM Customers'
	return HttpResponse(len(execute_query(query)))


def get_turnover(request):
	query = 'SELECT SUM(UnitPrice*Quantity) FROM invoice_items'
	return HttpResponse(f'{execute_query(query)[0][0]}')


'''
def list_of_orders(request):
	city = request.GET.get('city', '')
	state = request.GET.get('state', '')
	query = 'SELECT orders FROM invoices WHERE City =? AND State =?'
	records = execute_query(query, city, state)
	return HttpResponse(json.dumps(records))
'''


def execute_query(query, *args):
	db_path = os.path.join(os.getcwd(), 'chinook.db')
	connection = sqlite3.connect(db_path)
	curs = connection.cursor()
	curs.execute(query, args)
	return curs.fetchall()
