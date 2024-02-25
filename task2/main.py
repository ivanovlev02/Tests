import requests

class YA:
    def __init__(self, token):
        self.baseurl = 'https://cloud-api.yandex.net/'
        self.token = token
        self.headers = {'Authorization': f'OAuth {self.token}'}

    def disk_info(self):
        """Метод возвращает информацию о диске пользователя"""
        url = self.baseurl + 'v1/disk'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def is_file_or_folder_exist(self, path):
        """Метод проверяет существует ли указанный файл или папка"""
        url = self.baseurl + 'v1/disk/resources'
        params = {'path': path}
        resp = requests.get(url, headers=self.headers, params=params)
        return resp

    def create_folder(self, path):
        """Метод создает папку на яндекс диске"""
        url = self.baseurl + 'v1/disk/resources'
        params = {'path': path}
        resp = requests.put(url, headers=self.headers, params=params)
        return resp

    def delete_file_or_folder(self, path):
        """Метод удаляет файл или папку на яндекс диске"""
        url = self.baseurl + 'v1/disk/resources'
        params = {'path': path}
        resp = requests.delete(url, headers=self.headers, params=params)
        return resp
