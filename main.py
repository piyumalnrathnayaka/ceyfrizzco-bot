import telebot
from telebot import types
import json

# Bot Token
TOKEN = '8523105581:AAH83dotjrVIN4MU4QZwHwnQHudnn-m-5dU'
bot = telebot.TeleBot(TOKEN)

# Group ID
ORDER_GROUP_ID = "-1002207022228"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    
    # ඔයාගේ GitHub Pages ලින්ක් එක
    web_link = "https://piyumalnrathnayaka.github.io/ceyfrizzco-bot/" 
    web_app = types.WebAppInfo(web_link)
    
    btn_app = types.KeyboardButton(text="🛍️ Open CeyFrizzco Mall", web_app=web_app)
    markup.add(btn_app)
    
    welcome_text = (
        f"Hello {message.from_user.first_name}! 👋\n\n"
        "Welcome to CeyFrizzco PVT (LTD) Official Bot.\n"
        "Click the button below to start shopping from our Mini App!"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Mini App එකෙන් Order එකක් එන විට එය Group එකට යැවීම
@bot.message_handler(content_types=['web_app_data'])
def handle_order(message):
    data = json.loads(message.web_app_data.data) # ඇප් එකෙන් ලැබෙන බඩු ලැයිස්තුව
    
    # ඇණවුමේ විස්තර පෙළක් ලෙස සකස් කිරීම
    items_text = ""
    total_price = 0
    for item in data:
        items_text += f"• {item['name']} - Rs.{item['price']}\n"
        total_price += item['price']
    
    # පාරිභෝගිකයාට ස්තුති කිරීම
    bot.send_message(message.chat.id, f"✅ Order Received!\n\nTotal: Rs.{total_price}\nOur team will contact you soon.")
    
    # ඔබේ Telegram Group එකට ඇණවුම යැවීම
    admin_alert = (
        "🚨 *NEW MINI-APP ORDER*\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"👤 *Customer:* {message.from_user.first_name}\n"
        f"🆔 *User ID:* {message.from_user.id}\n\n"
        f"🛒 *Items:*\n{items_text}\n"
        f"💰 *Total Amount:* Rs.{total_price}\n"
        "━━━━━━━━━━━━━━━━━━"
    )
    bot.send_message(ORDER_GROUP_ID, admin_alert, parse_mode='Markdown')

print("CeyFrizzco 24/7 Bot is Running...")
bot.polling()

