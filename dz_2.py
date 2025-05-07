import requests
import unittest


class YandexDiskTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Чтение токена из файла
        with open('token.txt', 'r') as f:
            cls.TOKEN = f.read().strip()

        cls.headers = {
            'Authorization': f'OAuth {cls.TOKEN}'
        }
        cls.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        cls.folder_name = 'TestFolder'

    def test_create_folder_success(self):
        """Положительный тест: создание папки"""
        params = {
            'path': self.folder_name,
            'overwrite': True
        }

        response = requests.put(self.url, headers=self.headers, params=params)

        # Проверяем, что код ответа 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Проверяем, что папка появилась в списке файлов
        list_response = requests.get(self.url + '/children', headers=self.headers, params={'path': ''})
        self.assertIn(self.folder_name,
                      [item['name'] for item in list_response.json().get('_embedded', {}).get('items', [])])

    def test_create_folder_already_exists(self):
        """Отрицательный тест: попытка создать папку, которая уже существует"""
        params = {
            'path': self.folder_name,
            'overwrite': False  # Не перезаписываем существующую папку
        }

        response = requests.put(self.url, headers=self.headers, params=params)

        # Проверяем, что код ответа 409 (Conflict)
        self.assertEqual(response.status_code, 409)
        self.assertIn('Conflict', response.text)

    def test_create_folder_invalid_token(self):
        """Отрицательный тест: попытка создать папку с недействительным токеном"""
        invalid_token = 'INVALID_TOKEN'
        headers_invalid = {
            'Authorization': f'OAuth {invalid_token}'
        }

        params = {
            'path': 'AnotherTestFolder',
            'overwrite': True
        }

        response = requests.put(self.url, headers=headers_invalid, params=params)

        # Проверяем, что код ответа 401 (Unauthorized)
        self.assertEqual(response.status_code, 401)
        self.assertIn('Unauthorized', response.text)

    @classmethod
    def tearDownClass(cls):
        """Удаляем созданную папку после тестов"""
        params = {
            'path': cls.folder_name,
            'permanently': True  # Удаляем навсегда
        }

        requests.delete(cls.url, headers=cls.headers, params=params)


if __name__ == '__main__':
    unittest.main()
