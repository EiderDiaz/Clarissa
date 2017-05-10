import requests
import time 

url = "https://api.telegram.org/bot345011664:AAEzaG0p-MUahWspxpFehTOPpvOCicDCvUI/"


def get_updates_json(request):  

    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response
#recupera el id de la ultima conversasion
chat_id = get_chat_id(last_update(get_updates_json(url)))
##manda mensaje al al ultimo chat
send_mess(chat_id, 'Hola soy clarissa y estoy para servirle')

##es el loop para siempre contestar
def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        #chequea si update id tiene chat nuecos
        if update_id == last_update(get_updates_json(url))['update_id']:
            # manda mensaje al ultima conver que le mando mensaje
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'este mensaje se contesta automaticamente')
           #cambia el estado para que no se loopee y se mande menaje cuando si se reciva mensaje
           update_id += 1
    sleep(1)       

if __name__ == '__main__':  
    main()
