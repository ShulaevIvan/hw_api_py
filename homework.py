import requests

from pprint import pprint

import json

from requests.api import request

#1

class Super_hero():
    
    def get_character(self,token,character):
        self.character = character
        self.token = token
        char_obj = {}
        response = requests.get(f'https://superheroapi.com/api/{token}/search/{character}')
        all_data = response.json()

        results = all_data['results']
        char_name = results[0]['name']
        char_int = results[0]['powerstats']['intelligence']
        char_obj['name'] = char_name
        char_obj['char_int'] = char_int

        return char_obj

    def comparison(character_1,character_2,character_3):
        character_1_name = character_1['name']
        character_2_name = character_2['name']
        character_3_name = character_3['name']

        character_int_1 = int(character_1['char_int'])
        character_int_2 = int(character_2['char_int'])
        character_int_3 = int(character_3['char_int'])

        if character_int_1 > character_int_2 and character_int_1 > character_int_3:
            print(f'Наивысший интелект'+ f'{character_int_1}' + 'у '+ character_1['name'])
        elif character_int_2 > character_int_1 and character_int_2 > character_int_3:
            print(f'Наивысший интелект'+ f'{character_int_2}'  + 'у '+ character_2['name'])
        elif character_int_3 > character_int_1 and character_int_3 > character_int_2:
            print(f'Наивысший интелект '+ f'{character_int_3}' + ' у '+ character_3['name'])
        else:
            print('Одинаковый интелект')


hulk= Super_hero().get_character('2619421814940190', 'Hulk')
capitan = Super_hero().get_character('2619421814940190', 'Captain America')
thanos = Super_hero().get_character('2619421814940190', 'Thanos')

result = Super_hero.comparison(hulk, capitan, thanos)

# 2 YaUploader

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def authorization(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_link(self, file_path: str):
        upload_link = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.authorization()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_link, headers=headers, params=params)
        return response.json()

    def upload(self, file_path):
        href = self.upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))


class Stack():
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
        }

    def get_link(self):
        headers = self.get_headers()
        get_url = 'https://api.stackexchange.com/2.3/questions?fromdate=1634083200&todate=1634256000&order=desc&sort=activity&tagged=python&site=stackoverflow'
        response = requests.get(url=get_url, headers=headers)
        return response.json()

    def resolve(self):
        all_data = self.get_link()
        data_title = all_data['items']
        for title in data_title:
            pprint(title['title'])







if __name__ == '__main__':
    stack = Stack()
    stack.resolve()
    ya = YaUploader('AQAAAABZXUziAADLW0EqrmGpGEOdhl4v9d_4jRQ')
    ya.upload('test.txt')
    



        









