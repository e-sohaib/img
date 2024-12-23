import telebot


with open("/mnt/imageproccess/p.txt" , 'r') as r:
    token = r.read().strip()
    
bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=['start'])
def start(message) :
    bot.reply_to(message , "hi")
    
bot.polling(non_stop=True , timeout=25)
    