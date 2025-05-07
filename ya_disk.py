import requests

with open('token.txt', 'r') as f:
    TOKEN = f.read().strip()

headers = {
    'Authorization': f'OAuth {TOKEN}'
}

url = 'https://cloud-api.yandex.net/v1/disk/resources'

# Параметры для создания папки
params = {
    'path': 'НоваяПапка',
    'overwrite': True
}

response = requests.put(url, headers=headers, params=params)

if response.status_code == 201:
    print('Папка успешно создана')
else:
    print(f'Ошибка: {response.status_code} - {response.text}')
