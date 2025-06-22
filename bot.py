import telebot

# ✅ টেলিগ্রাম বট টোকেন
TOKEN = "7841877349:AAGQgDDyyizNSaxvxNWfplUkcnVhALWBYF8"

# 🤖 Bot তৈরি
bot = telebot.TeleBot(TOKEN)

# 🔰 Start কমান্ড হ্যান্ডলার
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 হ্যালো! আমি ইউটিউব লাইভ লিংক কনভার্ট করতে পারি! আমাকে একটি YouTube লাইভ লিংক পাঠান।")

# 🔗 যেকোনো মেসেজ হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    text = message.text.strip()

    # 🔍 Console Log
    print(f"👤 User: {first_name} (@{username}) | ID: {user_id}")
    print(f"💬 Message: {text}")
    print("-" * 50)

    # 🎯 YouTube লাইভ লিংক চেক
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

# ✅ Bot চালু
print("🤖 Bot চালু হয়েছে...")
bot.polling()
