import telegram

def welcomemsg(update, context):
    welcome = "Benvenuto su QuaranTips!\n\n"
    welcome += "Puoi usare questo bot per creare un diario di pensieri positivi e per ricevere consigli e informazioni utili in questo periodo di quarantena.\n"
    welcome += "Premi ---- per avere la lista delle funzionalità con la loro spiegazione"
    update.message.reply_text(welcome)

def helpmsg(update, context):
    """ Bot LineCommand: /help """

    help_text = 'Ecco una lista delle funzionalità di questo bot:\n\n' \
        'Puoi inserire dei *pensieri positivi* e rivederli quando vuoi, oppure chiedermi di fartene vedere uno casualmente.\n' \
        'Ecco come:\n' \
        '- Digita /pensiero seguito da uno spazio e dal tuo pensiero positivo per inserirlo nel database;\n' \
        '- /listapensieri per vedere la lista dei pensieri positivi che hai inserito finora;\n' \
        '- /pensierorandom per visualizzare uno tra i pensieri finora inseriti.\n\n'
    
    update.message.reply_text(help_text, parse_mode=telegram.ParseMode.MARKDOWN)