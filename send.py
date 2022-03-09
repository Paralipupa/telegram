import requests

#paralipupa_bot
api_token = '5129782717:AAHEFaNoP_gi3StZ_fSx_quV1aIoJV9aTUU'
#канал Алфинкомпани
chat_id ='-1001547029930 '
# chat_id ='@zaimzalog38bot'
url = 'https://api.telegram.org/bot{token}/sendMessage'\
.format(token=api_token)
param = dict(chat_id=chat_id, text='Hello, --- world')
text = requests.get(url, param)

print (text)