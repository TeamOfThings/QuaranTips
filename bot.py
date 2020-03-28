from telegram.ext import Updater
from telegram.ext import CommandHandler
import json
from sqlalchemy import func
from database import engine, Thought, create_tables
from message_reader import message_handler

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


# Def a method that only sends a message
def start(update, context):
    if not engine.dialect.has_table(engine, "thoughts"):
        create_tables()
    context.bot.send_message(chat_id=update.effective_chat.id, text="QuarantinTips!")

# Attach the method to a handler
    # The bot executes the method everytime it receives the \start command
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CommandHandler('save', message_handler))

# Start the bot
updater.start_polling()

print("**Finished successfully**")