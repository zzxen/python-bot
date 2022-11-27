#!/usr/bin/python3
#Libraries for telegram bot
from telegram import Bot
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler 
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import ContextTypes , CallbackQueryHandler

bot_token = "5870985444:AAGFyc8YG_aeO2KMBMC_kRkywJd-QpAj7Qs"
updater = Updater(bot_token , use_context = True)

#client side
def start(update : Update , context : CallbackContext):
    keyboard = [[InlineKeyboardButton("سفارش" , callback_data = "order")] , [InlineKeyboardButton("کانال اطلاع رسانی" , callback_data = "news")] , [InlineKeyboardButton("پشتیبانی" , callback_data = "support")] , [InlineKeyboardButton("گزارش" , callback_data = "report")] , [InlineKeyboardButton("درباره ربات" , callback_data = "about")]]
    update.message.reply_text("سلام به ربات پرداخت و سفارش سریع خوش آمدید چه کمکی میتونم بکنم؟" , reply_markup = InlineKeyboardMarkup(keyboard))

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == "order":
        query.message.reply_text("لیست \n : ‌ 1.خرید یوزر 5 عددی \n قیمت : 500 هزار تومان \n نوع : ‌VIP \n مدت اعتبار : 80 روز هر کاربر \n دارای پشتیبانی :‌ بله \n نوع پرداخت :‌ اینترنتی \n لینک پرداخت :‌ https://idpay.ir/orderonshop/5000000 \n ---------- \n توجه داشته باشید بعد پرداخت اسکرین شات تراکنش خود را به یوز زیر بفرستید و پک را دریافت نمایید \n ---------- \n توجه داشته باشید اطلاعات را درست درج نمایید و اسکرین شات را بفرستید در غیر این صورت تیم ما هیچ مسئولیتی را نمیپذیرد \n ارسال اسکرین شات به : ‌@SmartECAdmin")
    elif query.data == "news":
        query.message.reply_text("کانال اطلاع رسانی :‌ \n @SVPN2021‌")
    elif query.data == "support":
        query.message.reply_text("لیست پشتیبانی :\n @bvbloxic \n @SVPNSupport")
    elif query.data == "report":
        query.message.reply_text("لیست رسیدگی به گزارشات : \n @bvbloxic‌")
    elif query.data == "about":
        query.message.reply_text("این ربات توسط @bvbloxic برنامه نویسی شده است.")





updater.dispatcher.add_handler(CommandHandler('start' , start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()