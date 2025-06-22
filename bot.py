import telebot
from telebot import types
import os

# টোকেন নিচে বসাও
TOKEN = os.environ.get("7841877349:AAGQgDDyyizNSaxvxNWfplUkcnVhALWBYF8") or "7841877349:AAGQgDDyyizNSaxvxNWfplUkcnVhALWBYF8"
bot = telebot.TeleBot("7841877349:AAGQgDDyyizNSaxvxNWfplUkcnVhALWBYF8")

ADMIN_ID = 6124436525  # ← এখানে তোমার Telegram ID বসাও

# /start command
@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("📸 থাম্বনেইল দেখতে চাই")
    btn2 = types.KeyboardButton("📝 ভিডিও টাইটেল ও ডিসক্রিপশন")
    btn3 = types.KeyboardButton("🔗 লিংক কনভার্ট করতে চাই")

    markup.add(btn1, btn2)
    markup.add(btn3)

    bot.send_message(message.chat.id,
        "👋 স্বাগতম!\nআপনি কী করতে চান?", reply_markup=markup)

# হ্যান্ডল করা থাম্বনেইল
@bot.message_handler(func=lambda m: m.text == "📸 থাম্বনেইল দেখতে চাই")
def thumbnail_handler(message):
    bot.send_message(message.chat.id, "✅ দয়া করে ইউটিউব লিংক দিন আমি থাম্বনেইল দেখাবো।")

# হ্যান্ডল করা টাইটেল + ডিসক্রিপশন
@bot.message_handler(func=lambda m: m.text == "📝 ভিডিও টাইটেল ও ডিসক্রিপশন")
def title_description_handler(message):
    bot.send_message(message.chat.id, "✅ ইউটিউব লিংক দিন, আমি টাইটেল ও ডিসক্রিপশন দিচ্ছি।")

# হ্যান্ডল করা লিংক কনভার্ট
@bot.message_handler(func=lambda m: m.text == "🔗 লিংক কনভার্ট করতে চাই")
def convert_link_handler(message):
    bot.send_message(message.chat.id, "✅ ইউটিউব লাইভ লিংক দিন, আমি Watch ও Embed লিংকে কনভার্ট করে দিচ্ছি।")

# Default YouTube লিংক হ্যান্ডলার
@bot.message_handler(func=lambda message: "youtube.com/live/" in message.text)
def link_handler(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    text = message.text.strip()

    # ইউজারের মেসেজ তোমাকে ফরওয়ার্ড
    admin_msg = f"👤 {first_name} (@{username}) | ID: {user_id}\n💬 {text}"
    bot.send_message(ADMIN_ID, admin_msg)

    try:
        video_id = text.split("/live/")[-1].split("?")[0]
        watch_link = f"https://www.youtube.com/watch?v={video_id}"
        embed_link = f"https://www.youtube.com/embed/{video_id}"
        reply = f"🎯 Watch Link: {watch_link}\n💻 Embed Link: {embed_link}"
    except:
        reply = "❌ ভিডিও আইডি বের করা যায়নি।"

    bot.send_message(message.chat.id, reply)

print("🤖 Bot is running...")
bot.polling()
