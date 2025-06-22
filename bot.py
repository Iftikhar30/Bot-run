import telebot

TOKEN = "তোমার_বট_টোকেন_এখানে"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    text = message.text.strip()

    # 🔍 Console এ মেসেজ লগ করা
    print(f"👤 User: {first_name} (@{username}) | ID: {user_id}")
    print(f"💬 Message: {text}")
    print("-" * 50)

    # আগের মতো লিংক চেক ও রিপ্লাই
    if "youtube.com/live/" in text:
        if "/live/" in text:
            video_id = text.split("/live/")[-1].split("?")[0]
            watch_link = f"https://www.youtube.com/watch?v={video_id}"
            embed_link = f"https://www.youtube.com/embed/{video_id}"
            reply = f"🎯 Watch Link: {watch_link}\n💻 Embed Link: {embed_link}"
        else:
            reply = "❌ ভিডিও আইডি খুঁজে পাওয়া যায়নি।"
    else:
        reply = "🔗 অনুগ্রহ করে একটি YouTube লাইভ লিংক পাঠান।"

    bot.reply_to(message, reply)


print("🤖 Bot চালু হয়েছে...")
bot.polling()
