import requests


token = '5334926100:AAEOUjtyC4rfUMaEGa6oJpzp4yxe4HlzZx0'
chat_id = '-657978354'
text = 'Hello 13:51'

def sendTelegram():
	api = 'https://api.telegram.org/bot'
	method = api + token + '/sendMessage'

	req = requests.post(method, data={
		'chat_id': chat_id,
		'text': text
		})

sendTelegram()