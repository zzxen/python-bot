#!/usr/bin/python3from telegram.ext.updater import Updater
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler 
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from time import sleep

robot = "5802737472:AAFb0mSzPOk0V9p8jQA3_Xgp5jbZ_L8bKTk"
owner = "maeybeyes"
updater = Updater(token = robot , use_context = True)

def start(update : Update , context : CallbackContext):
    who = update.message.from_user.username
    print(who)
    if who == owner:
        keyboards = [
            [InlineKeyboardButton("Send point to last messages" , callback_data = "point")] , 
            [InlineKeyboardButton("My bio" , callback_data = "bio")] , 
        ]
        update.message.reply_text("How can i help my lord ?" , reply_markup = InlineKeyboardMarkup(keyboards))
    
    else:
        pass

def button(update : Update , context : CallbackContext) -> None :
    query = update.callback_query
    query.answer()
    if query.data == "point":
        query.message.edit_text(".")
        for i in range(100):
            query.message.reply_text(".")
    
    elif query.data == "bio":
        query.message.edit_text("My name is Moein , Iam 18 , Good to see you \n from : @maeybeyes")
    
    elif query.data == "vpnservice":
        query.message.edit_text("This bot want manager to sent VPN : @Onshophuge_bot")

    else:
        pass


updater.dispatcher.add_handler(CommandHandler("start" , start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
