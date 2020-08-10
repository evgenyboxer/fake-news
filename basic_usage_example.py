'''
You can read a news article from txt file and then store it in 'data'
'''

import requests

url = 'http://localhost:9000/predict'
data = 'the news are TRUE, we all must believe that!'
r = requests.post(url, data)

print(r.json())