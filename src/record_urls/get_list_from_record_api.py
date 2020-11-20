import os
import requests

user_id = 12345
url = 'http://radiorecord.ru/radioapi/stations'
answer = requests.get(url)
with open(os.path.abspath('files/raw_url.txt'), 'w', encoding='utf-8') as output_file:
    output_file.write(answer.text)