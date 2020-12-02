import os
import requests as rqs

user_id = 12345
url = 'http://radiorecord.ru/radioapi/stations'
answer = rqs.get(url)
#print(answer.json()["result"][0]["stream_320"])
b = answer.json()["result"]
for i in b:
    print("#"*10)
    print("#"*10)
    for j in i:
        print(j,end=" : ")
        print(str(i[j]))




# with open(os.path.abspath('files/raw_url.txt'), 'w', encoding='utf-8') as output_file:
#     output_file.write(answer.text)
