import csv
from flask import Flask
from faker import Faker

fake_ru = Faker('ru_Ru')


@app.route('/content')
def content():
    with open('requirements.txt', 'r') as file:
		out = file.read()
        return f'{out}'


# @app.route('/users')
def users():
	users = [(i, fake_ru.name(), fake_ru.ascii_free_email()) for i in range(1, 101)]
	return f'{users}'
		

print(users())
@app.route('/csv_read')
def csv_read():
    with open('hw.csv') as f:
        h_w = list(csv.reader(f))[1:]
        ah = sum([float(i[1]) for i in h_w]) / len(h_w)
        aw = sum([float(j[2]) for j in h_w]) / len(h_w)
        return f'The average height and weight: {ah} inches and {aw} lb'
