from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import telegram
import json
from sqlalchemy import func
from database import engine, Thought, create_tables
from thoughtmanager import ThoughtManager
from tips import tip, button
from pushNotifications import add_notification_handler
from informations import welcomemsg, helpmsg

"""
HELP
The Updater class continuously fetches new updates from telegram and passes them on to the Dispatcher class.
If you create an Updater object, it will create a Dispatcher for you and link them together with a Queue.
You can then register handlers of different types in the Dispatcher,
which will sort the updates fetched by the Updater according to the handlers you registered,
and deliver them to a callback function that you defined.
"""

# Init
with open("token.json", "r") as file:
    data = json.load(file)
    updater = Updater(token=data["bot_token"], use_context=True)

dispatcher = updater.dispatcher
tm = ThoughtManager()

if not engine.dialect.has_table(engine, "thoughts"):
        create_tables()



# # Def a method that only sends a message
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="QuarantinTips!")

# Attach the method to a handler
# The bot executes the method everytime it receives the \start command
updater.dispatcher.add_handler(CommandHandler("start", welcomemsg))
dispatcher.add_handler(CommandHandler("help", helpmsg))
updater.dispatcher.add_handler(CommandHandler('tip', tip))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('pensiero', tm.thought_handler))
updater.dispatcher.add_handler(CommandHandler('listapensieri', tm.get_thoughts_list))
updater.dispatcher.add_handler(CommandHandler('pensierorandom', tm.get_random_though))
updater.dispatcher.add_handler(CommandHandler('add_notification', add_notification_handler))



# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT

updater.idle()
