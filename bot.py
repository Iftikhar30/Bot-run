from telebot import types
import telebot

TOKEN = "7841877349:AAGQgDDyyizNSaxvxNWfplUkcnVhALWBYF8"
bot = telebot.TeleBot("7841877349:AAGQgDDyyizNSaxvxNWfplUkcnVhALWBYF8")

# প্রথমবার শুরু করলে কন্টাক্ট চাইবে
@bot.message_handler(commands=['start'])
def ask_for_contact(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button = types.KeyboardButton("📱 কন্টাক্ট শেয়ার করুন", request_contact=True)
    markup.add(button)
    bot.send_message(message.chat.id, "অনুগ্রহ করে আপনার কন্টাক্ট শেয়ার করুন:", reply_markup=markup)

# কন্টাক্ট পেলে সেভ করে রাখবে
@bot.message_handler(content_types=['contact'])
def save_contact(message):
    contact = message.contact
    bot.send_message(message.chat.id, f"ধন্যবাদ, {contact.first_name}! আপনার নাম্বার `{contact.phone_number}` সংরক্ষিত হয়েছে ✅", parse_mode='Markdown')
    # এখানে কন্টাক্ট ডাটাবেজে সেভ করতে পারো চাইলে
    # এরপর নরমাল চ্যাট পারমিশন দেওয়া হবে

# এরপরের মেসেজ হ্যান্ডলার: শুধু কন্টাক্ট দিলে এরপরই কাজ করবে
allowed_users = set()

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id

    # আগে কন্টাক্ট শেয়ার করেছে কিনা তা চেক করো
    if user_id not in allowed_users:
        bot.send_message(message.chat.id, "❌ আপনি এখনো কন্টাক্ট শেয়ার করেননি। অনুগ্রহ করে /start চাপুন এবং কন্টাক্ট শেয়ার করুন।")
        return
    
    # এরপর ইউটিউব লিংক প্রসেস
    text = message.text.strip()
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

# কন্টাক্ট শেয়ার করা হলে লিস্টে অ্যাড করো
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    user_id = message.from_user.id
    contact = message.contact.phone_number
    allowed_users.add(user_id)
    bot.send_message(message.chat.id, f"✅ কন্টাক্ট গ্রহণ করা হয়েছে: {contact}")
