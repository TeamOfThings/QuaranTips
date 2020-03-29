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
from telegram.ext import CommandHandler, CallbackQueryHandler

class TipList:
    """This class stores a fixed list of tips and randmly picks one
    """

    def __init__(self, tip_lst, link_lst):
        self.tip_list = tip_lst
        self.link_list = link_lst

    def pick_tip(self):
        idx = random.randint(0, len(self.tip_list)-1)
        return self.tip_list[idx]

    def pick_link(self):
        idx = random.randint(0, len(self.link_list)-1)
        return self.link_list[idx]


# Create object tips
book_tip = TipList([ "La saga di Harry Potter", "Il signore degli anelli", "La trilogia di Hunger Games",
                    "Il codice da Vinci", "I libri gialli di Agatha Christie, come Dieci piccoli indiani",
                    "Ready Player One", "Le cronache di Narnia", "La bussola d'oro", "Guida galaticca per autostoppisti",
                    "iniziare la saga delle Cronache del ghiaccio e del fuoco", "L'ombra del vento"],
                    ["https://www.ilpost.it/2020/03/13/sono-giorni-adatti-ai-libri-lunghi/",
                    "https://www.open.online/2020/03/11/coronavirus-10-libri-da-leggere-durante-la-quarantena/",
                    "https://www.ilpost.it/libri/"])

sport_tip = TipList([ "degli esercizi di stretching", "una corsa sul posto o step", "un allenamento online. Molti istruttori fanno esercizi in diretta",
                        ],
                    ["https://www.open.online/2020/03/14/coronavirus-dieci-esercizi-da-fare-per-allenarvi-in-casa-durante-la-quarantena/",
                    "https://www.my-personaltrainer.it/allenamento/palestra-casa.html"])


# Loggers 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)




def tip(update, context):
    """Creates tip buttons for the users"""
    # Definisce i bottoni
    keyboard = [[InlineKeyboardButton("Consiglio sportivo", callback_data='sport')],
                 [InlineKeyboardButton("Qualcosa da leggere", callback_data='books')]
                ]

    # Show buttons
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Seleziona una delle seguenti azioni', reply_markup=reply_markup)


def button(update, context):
    """Shows button messages """
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    # query.data == callback_data
    if query.data == "books":
        text = f"Ecco un buon libro da leggere: {book_tip.pick_tip()}\n\n"
        text = text + "Distrarsi dalle notizie durante la quarantena con un buon libro fa bene alla salute mentale.\n"
        text = text + f"Puoi trovare ulteriori suggerimenti su: {book_tip.pick_link()}"

    elif query.data == "sport":
        text = f"Non ti dimenticare di fare un po' di movimento, per esempio {sport_tip.pick_tip()}\n\n"
        text = text + "Lo sport, oltre a fare bene, ha anche una forte componente antidepressiva, importante durante questi giorni di quarantena.\n"
        text = text + f"Puoi trovare ulteriori suggerimenti su: {sport_tip.pick_link()}"

    else:
        pass

    query.edit_message_text(text=text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
