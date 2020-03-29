#!/usr/bin/env python


import telegram.ext
from telegram.ext import Updater
from tips import generic_tip


registered_users    = []


def messageCallback (context, user_id) :
    job = context.job
    
    if user_id in registered_users :
        reply_message   = "Ciao, ecco qui un suggerimento su cosa potresti fare!\n\n" + generic_tip.pick_tip ()
        print ("Sending this message:\n", reply_message)
        context.bot.send_message (chat_id=user_id, text=reply_message)
    else:
        job.schedule_removal()
        print ("Giob rimosso")


def add_notification_handler (updater, context) :
    user_id         = updater.message.from_user.id
    
    if user_id in registered_users :
        context.bot.send_message (chat_id=user_id, text="Operazione fallita: è stato già registrato un promemoria")
    else :
        lambda_message_callback = lambda ctxt : messageCallback (ctxt, user_id)
        context.job_queue.run_repeating (lambda_message_callback, interval=15, first=5)
        registered_users.insert (0, user_id)
        context.bot.send_message (chat_id=user_id, text="Operazione eseguita con successo")

    



def remove_notification_handler (updater, context) :
    user_id         = updater.message.from_user.id
    
    if user_id in registered_users :
        registered_users.remove (user_id)
        context.bot.send_message (chat_id=user_id, text="Operazione eseguita con successo")
    else:
        context.bot.send_message (chat_id=user_id, text="Operazione fallita: nessun promemoria attualmente registrato")