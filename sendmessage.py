import requests


token = '5190136746:AAGxE9tGCAz1ghL710dEeP2hiyHfPIP2zR8'
chat_id = '1636007800'
text = 'Test_2'


def sendTelegram():
	api = 'https://api.telegram.org/bot'
	method = api + token + '/sendMessage'

	req = requests.post(method, data={
		'chat_id': chat_id,
		'text': text})


sendTelegram()