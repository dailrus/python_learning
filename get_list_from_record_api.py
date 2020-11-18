import requests
user_id = 12345
url = 'http://radiorecord.ru/radioapi/stations'
answer = requests.get(url)
with open('output.txt', 'w') as output_file:
    output_file.write(answer.text)
