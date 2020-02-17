# Пример работы с web интерфейсом influx.db

import requests

DB_NAME = 'myfirstdb'

result = requests.get('http://localhost:8086/query?q=SHOW DATABASES').json()
print(result)

result = requests.post('http://localhost:8086/query', {'q': f'CREATE DATABASE {DB_NAME}'}).json()
print(result)

result = requests.get('http://localhost:8086/query?q=SHOW DATABASES').json()
print(result)

result = requests.post('http://localhost:8086/query', {'q': f'DROP DATABASE {DB_NAME}'}).json()
print(result)

result = requests.get('http://localhost:8086/query?q=SHOW DATABASES').json()
print(result)