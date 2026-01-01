import telebot
from telebot import types
import json

TOKEN = '8523105581:AAH83dotjrVIN4MU4QZwHwnQHudnn-m-5dU'
bot = telebot.TeleBot(TOKEN)
ORDER_GROUP_ID = "-1002207022228"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    
    # Mini App එක Open කරන විශේෂ බටන් එක
    # වෙබ් ඇප් එකේ URL එක විදියට ඔයාගේ Replit වෙබ් URL එක දාන්න ඕනේ
    web_info = types.WebAppInfo("https://YOUR-REPL-NAME.YOUR-USERNAME.repl.co") 
    btn_app = types.KeyboardButton(text="🛍️ Open CeyFrizzco Shop", web_app=web_info)
    
    markup.add(btn_app)
    bot.send_message(message.chat.id, "Welcome! Click the button below to open our Mini App store.", reply_markup=markup)

# Mini App එකෙන් දත්ත ලැබෙන විට ක්‍රියා කරන ආකාරය
@bot.message_handler(content_types=['web_app_data'])
def answer(webAppMes):
    data = json.loads(webAppMes.web_app_data.data) # ඇප් එකෙන් එන දත්ත
    items_list = "\n".join([f"- {i['name']} (Rs.{i['price']})" for i in data['items']])
    
    bot.send_message(webAppMes.chat.id, f"✅ Order Received!\nTotal: Rs.{data['total']}\nWe will contact you soon.")
    
    # Group එකට යැවීම
    admin_msg = (
        f"🚨 *NEW MINI-APP ORDER*\n"
        f"👤 Customer: {webAppMes.from_user.first_name}\n"
        f"🛒 Items:\n{items_list}\n"
        f"💰 Total: Rs.{data['total']}"
    )
    bot.send_message(ORDER_GROUP_ID, admin_alert, parse_mode='Markdown')

bot.polling()
