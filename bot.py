from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
import json
from tips import tip, button
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


# # Def a method that only sends a message
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="QuarantinTips!")

# Attach the method to a handler
    # The bot executes the method everytime it receives the \start command
updater.dispatcher.add_handler(CommandHandler('start', tip))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
