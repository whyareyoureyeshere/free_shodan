# -*- coding: utf-8 -*-
import shodan
import os
import time
import datetime

SHODAN_API_KEY = "PSKINdQe1GyxGgecYz2191H2JoS9qvgD"

api = shodan.Shodan(SHODAN_API_KEY)

def find_only_ip():
	try:
		results = api.search('''{s}'''.format(s=search))
		print('Results found: %s' % results['total'])
		for result in results['matches']:
				print('{}'.format(result['ip_str']))
	except (shodan.APIError)as e:
		print('Error: {}'.format(e))
def find():
	try:
		results = api.search('''{ts}'''.format(ts=search))
		print('Results found: %s' % results['total'])
		for result in results['matches']:
				print('IP: {}'.format(result['ip_str']))
				print(result['data'])
				print('')
	except (shodan.APIError)as e:
    print('Error: {}'.format(e))
		var = find()
print('''
╔═══╗╔═══╗╔═══╗╔═══╗   ╔═══╗╔╗ ╔╗╔═══╗╔═══╗╔═══╗╔═╗ ╔╗
║╔══╝║╔═╗║║╔══╝║╔══╝   ║╔═╗║║║ ║║║╔═╗║╚╗╔╗║║╔═╗║║║╚╗║║
║╚══╗║╚═╝║║╚══╗║╚══╗   ║╚══╗║╚═╝║║║ ║║ ║║║║║║ ║║║╔╗╚╝║
║╔══╝║╔╗╔╝║╔══╝║╔══╝   ╚══╗║║╔═╗║║║ ║║ ║║║║║╚═╝║║║╚╗║║
║║   ║║║╚╗║╚══╗║╚══╗   ║╚═╝║║║ ║║║╚═╝║╔╝╚╝║║╔═╗║║║ ║║║
╚╝   ╚╝╚═╝╚═══╝╚═══╝   ╚═══╝╚╝ ╚╝╚═══╝╚═══╝╚╝ ╚╝╚╝ ╚═╝
by lime
telegram: @appahe
''')
print('''Это бесплатный поисковик shodan
вот фильтры для поиска(с примером):
country:Страна
city:Город
geo:Гео локация
hostname:Хост
net:ip адрес
os:Операционная система
port:Порт

Ctrl+C для остановки пограммы''')



search = input('введите поисковой запрос==>')

question = input('''вам нужны только ip или все данные? данные/ip==>''')

if question == ("ip"):
	find_only_ip()
elif question == ("данные"):
	find()
else:
	print('Вы неправильно ввели данные. Закрытие программы...')
