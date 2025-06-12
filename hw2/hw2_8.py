import requests
import re
import random
import json

pattern = r'http(s)?://.+'

response = ''
url = ''
data = {}
method = None

while True:
    print()
    print(f'url: {url}')
    print('1 - URL\n2 - method\n3 - data\n4 - send request\n5 - clear request')
    act = int(input())
    match act:
        case 1:
            user_url = input('api url: ')
            if re.match(pattern, user_url):
                url = user_url
            else:
                print('invalid url')
                continue
        case 2:
            method_input = int(input('1 - GET\n2 - POST\n3 - PUT\n4 - PATCH\n5 - DELETE\n'))
            match method_input:
                case 1:
                    method = 'GET'
                case 2:
                    method = 'POST'
                case 3:
                    method = 'PUT'
                case 4:
                    method = 'PATCH'
                case 5:
                    method = 'DELETE'
                case _:
                    print('invalid method')
        
        case 3:
            user_id = random.randint(1, 1000)
            data['id'] = user_id
            user_name = input('your name: ')
            data['name'] = user_name
            while True:
                print('1 - new data\n2 - complete\n3 - clear data')
                data_act = int(input())
                match data_act:
                    case 1:
                        new_data_key = input('new data key: ')
                        new_data_value = input(f'{new_data_key}: ')
                        data[new_data_key] = new_data_value
                    case 2:
                        break
                    case 3:
                        data = {}
                        data['id'] = user_id
                        data['name'] = user_name
        
        case 4:
            if not url or not method:
                print('Set URL and method first')
                continue
            try:
                if method == 'GET':
                    temp_response = requests.get(url, params=data)
                    result = temp_response.json()
                    if not result:
                        response = requests.get(url, params=None)
                    else:
                        response = temp_response
                elif method == 'POST':
                    response = requests.post(url, json=data)
                elif method == 'PUT':
                    response = requests.put(url, json=data)
                elif method == 'PATCH':
                    response = requests.patch(url, json=data)
                elif method == 'DELETE':
                    response = requests.delete(url, json=data)
                else:
                    print('invalid method')
                    continue

                print('Requesting:', response.url)

                try:
                    result = response.json()
                except json.JSONDecodeError:
                    result = response.text

                with open('response.json', 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=4, ensure_ascii=False)
                
                print('request complete')
            
            except Exception as e:
                print('Error:', e)
        
        case 5:
            url = ''
            data = {}
            method = None