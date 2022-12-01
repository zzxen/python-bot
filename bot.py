#!/usr/bin/python3
#Libraries for telegram bot
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler 
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
import sqlite3

bot_token = "5870985444:AAEf1Z24xBoB0uyK3Kxjf0cK8J_gxsurMlM"
updater = Updater(bot_token , use_context = True)
#owner[0] and real-managers[1]
auth = ["bvbloxic"]
#managers informations
username = {}
#black list of managers
black_list = []

#client side
def start(update : Update , context : CallbackContext):
    user = update.message.chat["username"]
    if user in auth:
        keyboards = [
            [InlineKeyboardButton("خرید فیلترشکن" , callback_data = "order")] , 
            [InlineKeyboardButton("کانال اطلاع رسانی" , callback_data = "news")] , 
            [InlineKeyboardButton("پشتیبانی" , callback_data = "support")] , 
            [InlineKeyboardButton("گزارش" , callback_data = "report")] , 
            [InlineKeyboardButton("درباره ربات" , callback_data = "about")] , 
            [InlineKeyboardButton("لیست نمایندگی ها" , callback_data = "list")] ,
        ]
        update.message.reply_text("سلام به ربات پرداخت و سفارش سریع خوش آمدید چه کمکی میتونم بکنم؟" , reply_markup = InlineKeyboardMarkup(keyboards))
    else:
        if user in username:
            if user in black_list:
                #message
                update.message.reply_text("نماینده محترم شما از طرف مدیریت مسدود شده اید لطفا با پشتیبانی در تماس باشید \n @bvbloxic \n @SmartECAdmin")
            else:
                keyboards = [
                    [InlineKeyboardButton("خرید یوزر فیلترشکن" , callback_data = "order")] , 
                    [InlineKeyboardButton("کانال اطلاع رسانی" , callback_data = "news")] , 
                    [InlineKeyboardButton("پشتیبانی" , callback_data = "support")] , 
                    [InlineKeyboardButton("گزارش" , callback_data = "report")] , 
                    [InlineKeyboardButton("درباره ربات" , callback_data = "about")] , 
                    [InlineKeyboardButton("اطلاعات" , callback_data = "info")] , 
                ]
                update.message.reply_text("سلام به ربات پرداخت و سفارش سریع خوش آمدید چه کمکی میتونم بکنم؟" , reply_markup = InlineKeyboardMarkup(keyboards))
        else:
            update.message.reply_text("شما به عنوان نماینده ثبت نشده اید لطفا با پشتیبانی تماس بگیرید یا حضوری مراجعه کنید. \n @bvbloxic \n @SmartECAdmin")

def add_real_manager(update : Update , context : CallbackContext):
    #verify owner
    authantication = update.message.chat["username"]
    if authantication == auth[0]:
        #understand owner commands
        owner_commands = update.message.text
        splite = owner_commands.split()
        #check real-manager status
        if splite[1] in auth:
            #message
            update.message.reply_text(f"مدیر {splite[1]} در حا حاضر مدیر است")
        else:
            auth.append(splite[1])
            update.message.reply_text(f"نماینده {splite[1]} به مدیریت برگزیده شد")
    else:
        pass

def delete_real_manager(update : Update , context : CallbackContext):
    #verify owner
    authantication = update.message.chat["username"]
    if authantication == auth[0]:
        #understand owner commands
        owner_commands = update.message.text
        splite = owner_commands.split()
        #check real-manager status
        if splite[1] in auth:
            #remove
            auth.remove(splite[1])
            #message 
            update.message.reply_text(f"مدیر {splite[1]} از لیست مدیریت حذف گردید")
        else:
            #message
            update.message.reply_text(f"یوزر {splite[1]} مدیر نیست")
    else:
        pass


def add_managers(update : Update , context : CallbackContext):
    try:
        #verify owner
        authantication = update.message.chat["username"]
        if authantication in auth:
            #understand owner commands
            user_commands = update.message.text
            splite = user_commands.split()
            #add information to temporary database
            username[splite[1]] = f"نام نمایندگی :‌ {splite[2]} \n شماره همراه : {splite[3]} \n وضعیت : {splite[4]} \n اگر اطلاعات نشان داده شده اشتباه است یا ایراد دارد حتما با پشتیبانی تماس بگیرید \n @bvbloxic"
            #message
            update.message.reply_text("اطلاعات نمایندگی جدید با موفقیت ثبت شد")
            #add to database
            database = sqlite3.connect("info.db")
            curser = database.cursor()
            sql_data = f""" INSERT INTO MANAGERS (username , nameandfamily , phone) VALUES ("{splite[1]}" , "{splite[2]}" , "{splite[3]}")  """
            curser.execute(sql_data)
            database.commit()
            database.close()
        else:
            pass
    except IndexError:
        update.message.reply_text("لطفا تمام اطلاعات را بصورت زیر وارد کنید :‌\n /add <username> <name> <phonenumber> <active/deactive>")

def edit_managers_infomations(update : Update , context : CallbackContext):
    #verify owner
    authantication = update.message.chat["username"]
    if authantication in auth:
        #understand owner commands
        user_commands = update.message.text
        splite = user_commands.split()
        #edit informations on temporary database
        username[splite[1]] = f"نام نمایندگی :‌ {splite[2]} \n شماره همراه : {splite[3]} \n وضعیت :‌ {splite[4]} \n اگر اطلاعات نشان داده شده اشتباه است یا ایراد دارد حتما با پشتیبانی تماس بگیرید \n @bvbloxic"
        #message
        update.message.reply_text("اطلاعات با موفقیت تغییر یافت.")
    else:
        pass

def delete_managers(update : Update , context : CallbackContext):
    #verify owner
    authantication = update.message.chat["username"]
    if authantication in auth:
        #understand owner commands
        user_commands = update.message.text
        splite = user_commands.split()
        #check manager status
        if splite[1] in username:
            #delete from temparory database
            delete = username.pop(splite[1])
            #message
            update.message.reply_text(f"اطلاعات نمایندگی {splite[1]} با موفقیت حذف گردید")
        else:
            update.message.reply_text(f"یوزر {splite[1]} نماینده نمیباشد")
    else:
        pass

def enable_managers(update : Update , context : CallbackContext):
    #verify owner
    authantication = update.message.chat["username"]
    if authantication in auth:
        #understand owner commands
        user_commands = update.message.text
        splite = user_commands.split()
        #check manager status if in black list
        if splite[1] in black_list:
            black_list.remove(splite[1])
            #message
            update.message.reply_text(f"نماینده {splite[1]} با موفقیت فعال شد")
        else:
            #message
            update.message.reply_text(f"نماینده {splite[1]} فعال است")
    else:
        pass

def disable_managers(update : Update , context : CallbackContext):
    #verify owner
    authantication = update.message.chat["username"]
    if authantication in auth:
        #unserstand owner commands
        user_commands = update.message.text
        splite = user_commands.split()
        #check managers status in black list
        if splite[1] in black_list:
            #message
            update.message.reply_text(f"نماینده {splite[1]} در حال حاضر غیرفعال است")
        else:
            #add manager to black list
            black_list.append(splite[1])
            #message
            update.message.reply_text(f"نماینده {splite[1]}‌ غیرفعال شد")
    else:
        pass



def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    user = query.message.chat["username"]
    
    if user in auth:
        if query.data == "order":
            query.message.edit_text("لیست \n : ‌ 1.خرید یوزر 5 عددی \n قیمت : 500 هزار تومان \n نوع : ‌VIP \n مدت اعتبار : 80 روز هر کاربر \n دارای پشتیبانی :‌ بله \n نوع پرداخت :‌ اینترنتی \n لینک پرداخت :‌ 6037998211908040 (ابوالفضل فضل اله زاده) \n ---------- \n توجه داشته باشید بعد پرداخت اسکرین شات تراکنش خود را به یوز زیر بفرستید و پک را دریافت نمایید \n ---------- \n توجه داشته باشید اطلاعات را درست درج نمایید و اسکرین شات را بفرستید در غیر این صورت تیم ما هیچ مسئولیتی را نمیپذیرد \n ارسال اسکرین شات به : ‌@SmartECAdmin")
        elif query.data == "news":
            query.message.edit_text("کانال اطلاع رسانی :‌ \n @SVPN2021‌")
        elif query.data == "support":
            query.message.edit_text("لیست پشتیبانی :\n @bvbloxic \n @SVPNSupport")
        elif query.data == "report":
            query.message.edit_text("لیست رسیدگی به گزارشات : \n @bvbloxic‌")
        elif query.data == "about":
            query.message.edit_text("این ربات توسط @bvbloxic برنامه نویسی شده است.")
        elif query.data == "list":
            if username.keys():
                users_list = list(username.keys())
                users = "\n@".join(users_list)
                query.message.edit_text(f"اسامی نمایندگان : \n @{users}")
            else:
                query.message.edit_text("در حال حاضر هیچ نماینده فعالی وجود ندارد")
        elif query.data == "info": 
            query.message.edit_text(username[user])
    else:
        if user in username:
            if user in black_list:
                query.message.reply_text("نماینده محترم شما از طرف مدیریت مسدود شده اید لطفا با پشتیبانی در تماس باشید \n @bvbloxic \n @SmartECAdmin")
            
            else:
                if query.data == "order":
                   query.message.edit_text("لیست \n : ‌ 1.خرید یوزر 5 عددی \n قیمت : 500 هزار تومان \n نوع : ‌VIP \n مدت اعتبار : 80 روز هر کاربر \n دارای پشتیبانی :‌ بله \n نوع پرداخت :‌ اینترنتی \n لینک پرداخت :‌ https://idpay.ir/orderonshop/5000000 \n ---------- \n توجه داشته باشید بعد پرداخت اسکرین شات تراکنش خود را به یوز زیر بفرستید و پک را دریافت نمایید \n ---------- \n توجه داشته باشید اطلاعات را درست درج نمایید و اسکرین شات را بفرستید در غیر این صورت تیم ما هیچ مسئولیتی را نمیپذیرد \n ارسال اسکرین شات به : ‌@SmartECAdmin")
                elif query.data == "news":
                    query.message.edit_text("کانال اطلاع رسانی :‌ \n @SVPN2021‌")
                elif query.data == "support":
                    query.message.edit_text("لیست پشتیبانی :\n @bvbloxic \n @SVPNSupport")
                elif query.data == "report":
                    query.message.edit_text("لیست رسیدگی به گزارشات : \n @bvbloxic‌")
                elif query.data == "about":
                    query.message.edit_text("این ربات توسط @bvbloxic برنامه نویسی شده است.")
                elif query.data == "info":
                    query.message.edit_text(username[user])
        else:
            query.message.edit_text("شما به عنوان نماینده ثبت نشده اید لطفا با پشتیبانی تماس بگیرید یا حضوری مراجعه کنید. \n @bvbloxic \n @SmartECAdmin")

         


updater.dispatcher.add_handler(CommandHandler('start' , start))
updater.dispatcher.add_handler(CommandHandler('addreal' , add_real_manager))
updater.dispatcher.add_handler(CommandHandler('deletereal' , delete_real_manager))
updater.dispatcher.add_handler(CommandHandler('add' , add_managers))
updater.dispatcher.add_handler(CommandHandler('edit' , edit_managers_infomations))
updater.dispatcher.add_handler(CommandHandler('delete' , delete_managers))
updater.dispatcher.add_handler(CommandHandler('enable' , enable_managers))
updater.dispatcher.add_handler(CommandHandler('disable' , disable_managers))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()