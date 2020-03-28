def message_handler(update, context):
    user_says = " ".join(context.args)
    update.message.reply_text("Il tuo messaggio è stato salvato")
    #update.message.reply_text("You said: " + user_says)

