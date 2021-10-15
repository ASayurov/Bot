import telebot
import config
import btc

bot = telebot.TeleBot(config.TOKEN)
curse = btc.btc_r

@bot.message_handler(commands=['start'])
def welcome(message):
  bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот который покажет курс биткоина, он равен {2}'.format(message.from_user, bot.get_me(), curse),parse_mode='html')

@bot.message_handler(content_types=['text'])
def start(message):
	bot.send_message(message.chat.id, message.text)

# Start
bot.polling(none_stop=True)