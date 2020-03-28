#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards.
"""
import logging
import json
import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

class BookTip:

    def __init__(self):

        self.books = [
            "La saga di Harry Potter",
            "Il signore degli anelli",
            "La trilogia di Hunger Games"
        ]


    def pick(self):
        idx = random.randint(0, len(self.books)-1)
        return self.books[idx]


class SportTip:

    def __init__(self):

        self.sports = [
            "degli esercizi di stretching",
            "una corsa sul posto o step",
            "un allenamento online. Molti istruttori fanno esercizi in diretta"
        ]


    def pick(self):
        idx = random.randint(0, len(self.sports)-1)
        return self.sports[idx]


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Read token
with open("token.json", "r") as file:
    data = json.load(file)
    token = data["bot_token"]


# Create obejct tips
book_tip = BookTip()
sport_tip = SportTip()

def tip(update, context):
    # Definisce i bottoni
    keyboard = [[InlineKeyboardButton("Consiglio sportivo", callback_data='sport')],
                 [InlineKeyboardButton("Qualcosa da leggere", callback_data='books')]
                ]

    # Show buttons
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Seleziona una delle seguenti azioni', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    # query.data == callback_data
    if query.data == "books":
        text = f"Ecco un buon libro da leggere: {book_tip.pick()}\n\n"
        text = text + "Distrarsi dalle notizie durante la quarantena con un buon libro fa bene alla salute mentale.\n"
        text = text + "Leggi altri consigli su: https://www.ilpost.it/2020/03/16/consigli-psicologici-coronavirus/"

    elif query.data == "sport":
        text = f"Non ti dimenticare di fare un po' di movimento, per esempio {sport_tip.pick()}\n\n"
        text = text + "Lo sport, oltre a fare bene, ha anche una forte componente antidepressiva, importante durante questi giorni di quarantena.\n"
        text = text + "Leggi di più su: https://www.ilpost.it/2020/03/16/consigli-psicologici-coronavirus/"

    else:
        pass

    query.edit_message_text(text=text)


def help(update, context):
    update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler('start', tip))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()