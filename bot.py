import telebot
import os
from fingerprint import finger


with open("/mnt/imageproccess/p.txt" , 'r') as r:
    token = r.read().strip()
    
bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=['start'])
def start(message) :
    bot.reply_to(message , "hi")
    
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        # گرفتن فایل ID از عکس
        file_id = message.photo[-1].file_id  # بزرگترین سایز عکس
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # ذخیره عکس در سیستم
        file_name = f"{file_id}.jpg"
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "عکس شما دریافت و ذخیره شد.")
        finger(file_name)
        # اینجا می‌تونید تصویر ذخیره‌شده رو پردازش کنید
        with open(f"res-{file_name}", 'rb') as result:
            bot.send_photo(message.chat.id , result)
        os.remove(f"res-{file_name}")
    except Exception as e:
        bot.reply_to(message, f"مشکلی پیش آمد: {e}")
        print(f"Error: {e}")

    
bot.polling(non_stop=True , timeout=25)
    