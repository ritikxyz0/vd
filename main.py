import telebot
import os
from telebot.types import ChatMember
from config import API_TOKEN, GROUP_ID
from downloader import download_video_from_url

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome! This bot is made by @RitikXyz099\nSend me any YouTube/Instagram/Facebook video link!")

@bot.message_handler(func=lambda message: True)
def handle_download(message):
    try:
        member = bot.get_chat_member(GROUP_ID, message.from_user.id)
        if member.status in ['left', 'kicked']:
            bot.reply_to(message, "Pehle ja ke join kar lavde 😂 https://t.me/+j-V8XNgEHhRkMGRl")
            return
    except Exception:
        bot.reply_to(message, "Pehle ja ke join kar lavde 😂 https://t.me/+j-V8XNgEHhRkMGRl")
        return

    url = message.text.strip()
    bot.reply_to(message, "Downloading... ⏳")

    try:
        filename = download_video_from_url(url)
        with open(filename, 'rb') as video:
            bot.send_video(message.chat.id, video, caption="✅ Video Downloaded!\n👨‍💻 Developer: @RitikXyz099")
        os.remove(filename)
    except Exception as e:
        bot.reply_to(message, f"❌ Failed: {str(e)}")

bot.polling()
