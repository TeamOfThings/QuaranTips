import telegram

def welcomemsg(update, context):
    welcome = "Benvenuto su QuaranTips!\n\n"
    welcome += "Puoi usare questo bot per creare un diario di pensieri positivi e per ricevere consigli e informazioni utili in questo periodo di quarantena.\n"
    welcome += "Usa il comando /help per avere la lista delle funzionalità con la loro spiegazione"
    update.message.reply_text(welcome)

def helpmsg(update, context):
    """ Bot LineCommand: /help """

    help_text = 'Ecco una lista delle funzionalità di questo bot:\n\n' \
        'Puoi inserire dei *pensieri positivi* e rivederli quando vuoi, oppure chiedermi di fartene vedere uno casualmente.\n' \
        'Ecco come:\n' \
        '- Digita /pensiero seguito da uno spazio e dal tuo pensiero positivo per inserirlo nel diario;\n' \
        '- /listapensieri per vedere la lista dei pensieri positivi che hai inserito finora;\n' \
        '- /pensierorandom per visualizzare uno tra i pensieri finora inseriti.\n\n' \
        'Puoi ricevere delle notifiche giornaliere che ti motivino ad esplorare una delle funzionalità di questo bot:\n' \
        '- /promemoriagiornaliero crea un promemoria che quotidianamente ti invia un consiglio per la quarantena;\n'\
        '- /cancellapromemoria cancella il promemoria.\n\n' \
        'Puoi ricevere dei consigli e delle informazioni utili:\n'\
        '- /tip ti mostra delle categorie su cui ricevere un piccolo consiglio.\n'
    
    update.message.reply_text(help_text, parse_mode=telegram.ParseMode.MARKDOWN)