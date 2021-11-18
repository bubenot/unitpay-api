import requests
import json

email = ""
token = ""

class Unitpay(email, token):
	#Кабинет API
	def checkBalance(self):
		if __name__ == '__main__':
			data = {
				"method": "getPartner",
				"params[login]": email,
				"params[secretKey]": token
			}
			resp = requests.get("https://unitpay.ru/api", params=data)
			resp_result = resp.json()
			try:
				resp_result['result']
			except KeyError:
				if resp_result['error']['code'] == -32000:
					print(" > [UnitPay] Ошибка авторизации")
				elif resp_result['error']['code'] == -32602:
					print(" > [UnitPay] Ошибочные параметры запроса (разраб. кривожоп)")
				elif resp_result['error']['code'] == -32603:
					print(" > [UnitPay] Внутренняя техническая ошибка")
				else:
					print(" > [UnitPay] Неизвестная ошибка")
			else:
				print(
					"Пользователь: " + resp_result['result']['email'] +
					"\n" + "Баланс: " + resp_result['result']['balance'] + " руб.")
with open('settings.json') as read_file:
	config = json.load(read_file)

test = Unitpay(config['email'], config['token'])
test.checkBalance()