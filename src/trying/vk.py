import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType

import random

session = vk_api.VkApi(token='a43322c9617ca9dd301061ecbf3aaf3d48bd3dd321e4ab762d2a75a6b56b7660353a3e4d056b884450cd7')
longpoll = VkLongPoll(session)
vk = session.get_api()

import datetime


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        random_id = vk_api.utils.get_random_id()	
        if event.text == 'Время' or event.text == 'Привет' or event.text == 'привет' or event.text == 'время': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Московское время: ' + str(datetime.datetime.now().strftime("%H:%M")),
                    random_id = random_id

		)
            elif event.from_chat: #Если написали в Беседе
                vk.messages.send( #Отправляем собщение
                    chat_id=event.chat_id,
                    message='Московское время: ' + str(datetime.datetime.now().strftime("%H:%M")),
                    random_id=random_id
                    
		)
        elif event.text == 'рандомное число' or event.text == 'рандом':
            if event.from_user:
                randnum = random.randint(1, 100000000)
                vk.messages.send(user_id=event.user_id, message=randnum, random_id=random_id)
                print('Рандомное число {0} успешно отправлено пользователю {1}'.format(randnum, event.user_id))
            elif event.from_group:
                randnum = random.randint(1, 100000000)
                vk.messages.send(chat_id=event.chat_id, message=randnum, random_id=random_id)
                print('Рандомное число {0} успешно в беседу {1}'.format(randnum, event.group_id))
        elif event.text == 'temp':
            if event.from_user:
                vk.messages.send(random_id=random_id, user_id=event.user_id, message='Температура в серверной {0} градусов по цельсию'.format(temp[2:6]))
                print('Пользователь {0} получли температуру в серверной'.format(event.user_id))
            elif event.from_group:
                vk.messages.send(random_id=random_id, chat_id=event.group_id, message='Вам недоступна данная команда')
                print('В чате {0} попытались получить температуру'.format(event.group_id))    

        
        else:
            if event.from_user:
                vk.messages.send(user_id=event.user_id, message='Не знаю таких слов', random_id=random_id)
                print('Ошибка отправлена пользователю {0}'.format(event.user_id))
            elif event.from_group:
                vk.message.send(chat_id=event.chat_id, message='Я тупой и не знаю таких слов', random_id=random_id)
                print('Ошибка отправлена пользователю {0}'.format(event.group_id))
        