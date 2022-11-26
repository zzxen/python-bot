#!/usr/bin/python3
#Libraries for telegram bot
from telegram import Bot
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler 
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import telegram

bot_token = "5870985444:AAGFyc8YG_aeO2KMBMC_kRkywJd-QpAj7Qs"
updater = Updater(bot_token , use_context = True)

#client side
def start(update : Update , context : CallbackContext):
    update.message.reply_text("سلام به ربات پرداخت و سفارش سریع خوش آمدید چه کمکی میتونم بکنم؟")

def help(update : Update , context : CallbackContext):
    update.message.reply_text("لیست کار هایی که میتونم براتون انجام بدم :‌\n /order --- سفارش کالا \n /help --- لیست کارها \n /news اخبارات جدید در مورد کالا ها و قیمت ها \n /support --- پشتیبانی \n /report --- گزارش کردن مشکلات \n /register --- درخواست ثبت نام نمایندگی")

def order(update : Update , context : CallbackContext):
    update.message.reply_text("لیست \n : ‌ 1.خرید یوزر 5 عددی \n قیمت : 500 هزار تومان \n نوع : ‌VIP \n مدت اعتبار : 80 روز هر کاربر \n دارای پشتیبانی :‌ بله \n نوع پرداخت :‌ اینترنتی \n لینک پرداخت :‌ https://idpay.ir/orderonshop/5000000 \n ---------- \n توجه داشته باشید بعد پرداخت اسکرین شات تراکنش خود را به یوز زیر بفرستید و پک را دریافت نمایید \n ---------- \n توجه داشته باشید اطلاعات را درست درج نمایید و اسکرین شات را بفرستید در غیر این صورت تیم ما هیچ مسئولیتی را نمیپذیرد \n ارسال اسکرین شات به : ‌@SmartECAdmin") 

def news(update : Update , context : CallbackContext) : 
    update.message.reply_text("برای دریافت اخبار های قبلی در کانال عضو شوید : \n @SVPN2021‌")

def support(update :Update , context : CallbackContext):
    update.message.reply_text("لیست پشتیبانی :\n @bvbloxic \n @SVPNSupport")

def report(update : Update , context : CallbackContext):
    update.message.reply_text("لیست رسیدگی به گزارشات : \n @bvbloxic‌")

def register(update : Update , context : CallbackContext):
    update.message.reply_text("به زودی این امکان دردسترس خواهد بود.")

updater.dispatcher.add_handler(CommandHandler('start' , start))
updater.dispatcher.add_handler(CommandHandler('help' , help))
updater.dispatcher.add_handler(CommandHandler('order' , order))
updater.dispatcher.add_handler(CommandHandler('news' , news))
updater.dispatcher.add_handler(CommandHandler('support' , support))
updater.dispatcher.add_handler(CommandHandler('report' , report))
updater.dispatcher.add_handler(CommandHandler('register' , register))