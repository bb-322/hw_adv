import random
import requests

resourses = {   
    '/posts/': 100,
    '/comments/': 500,
    '/albums/': 100,
    '/photos/': 5000,
    '/todos/': 200,
    '/users/': 10
}
res_keys = []
for key, val in resourses.items():
    res_keys.append(key)
random_key = random.choice(res_keys)
random_res= random_key + str(random.randint(1, resourses[random_key]))
response = requests.get('https://jsonplaceholder.typicode.com' + random_res)
print(response.text)