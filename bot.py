import telebot
from telebot import types

# ✅ টেলিগ্রাম বট টোকেন
TOKEN = "7841877349:AAGQgDDyyizNSaxvxNWfplUkcnVhALWBYF8"

bot = telebot.TeleBot(TOKEN)

# 📌 অনুমতি পাওয়া ইউজার আইডি স্টোর
allowed_users = set()

# ✅ /start কমান্ড — কন্টাক্ট পারমিশন চায়
@bot.message_handler(commands=['start'])
def ask_contact_permission(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    contact_button = types.KeyboardButton("📱 কন্টাক্ট শেয়ার করুন", request_contact=True)
    markup.add(contact_button)
    bot.send_message(message.chat.id, "🚨 অনুগ্রহ করে আপনার কন্টাক্ট শেয়ার করুন বট ব্যবহারের আগে:", reply_markup=markup)

# ✅ কন্টাক্ট পেলে অনুমতি লিস্টে যোগ করে
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    user_id = message.from_user.id
    contact = message.contact.phone_number
    allowed_users.add(user_id)
    bot.send_message(message.chat.id, f"✅ ধন্যবাদ! আপনার কন্টাক্ট গ্রহণ করা হয়েছে: {contact}\nএখন আপনি YouTube লাইভ লিংক পাঠাতে পারেন।")

# ✅ YouTube লিংক প্রসেস করা হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    text = message.text.strip()

    # 👮 কন্টাক্ট না দিলে ব্লক করো
    if user_id not in allowed_users:
        bot.send_message(message.chat.id, "❌ আপনি এখনো কন্টাক্ট শেয়ার করেননি। অনুগ্রহ করে /start দিন এবং কন্টাক্ট শেয়ার করুন।")
        return

    # 🔍 ইউটিউব লাইভ লিংক চেক
    if "youtube.com/live/" in text:
        try:
            video_id = text.split("/live/")[-1].split("?")[0]
            watch_link = f"https://www.youtube.com/watch?v={video_id}"
            embed_link = f"https://www.youtube.com/embed/{video_id}"
            reply = f"🎯 Watch Link: {watch_link}\n💻 Embed Link: {embed_link}"
        except:
            reply = "❌ ভিডিও আইডি প্রসেস করতে সমস্যা হয়েছে।"
    else:
        reply = "🔗 অনুগ্রহ করে একটি সঠিক YouTube লাইভ লিংক পাঠান।"

    bot.reply_to(message, reply)

# ✅ বট চালু
print("🤖 Bot চালু হয়েছে...")
bot.polling()
