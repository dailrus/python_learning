import os
import requests

user_id = 12345
url = 'http://radiorecord.ru/radioapi/stations'
answer = requests.get(url)
#print(answer.json()["result"][0]["stream_320"])
b = answer.json()["result"][0]
for i in b:
    print(i,end=" = ")
    print(str(b[i]))
# with open(os.path.abspath('files/raw_url.txt'), 'w', encoding='utf-8') as output_file:
#     output_file.write(answer.text)
