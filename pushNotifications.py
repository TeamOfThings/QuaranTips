#!/usr/bin/env python


import telegram.ext
from telegram.ext import Updater
from tips import book_tip, sport_tip


def add_notification_handler (updater, context) :
    user_message    = " ".join (context.args)
    user_id         = updater.message.from_user.id

    if user_message == "book":
        messagePicker   = lambda : "Potresti leggere: " + book_tip.pick ()
        add_notification (context, user_id, messagePicker)
    elif user_message == "sport":
        messagePicker   = lambda : "Ecco un'esercizio da fare: " + sport_tip.pick ()
        add_notification (context, user_id, messagePicker)
    else:
        updater.message.reply_text ("Categoria sconosciuta")


def add_notification (context, chatId, messagePicker, initialDelay=0, delay=3600) :
    messageCallback = lambda ctxt : ctxt.bot.send_message (chat_id=chatId, text=messagePicker())
    context.job_queue.run_repeating (messageCallback, interval=delay, first=initialDelay)
