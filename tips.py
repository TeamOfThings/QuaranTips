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

generic_tip = TipList(["Limita il tuo accesso alle notizie riguardanti il coronavirus, che può causare depressione o attacchi di panico \n\nhttps://www.bbc.com/news/health-51873799",
                        "Prova a coltivare un hobby che hai da sempre rimandato, sempre che la quarantena lo permetta \n\nhttps://www.fondazioneveronesi.it/magazine/articoli/lesperto-risponde/coronavirus-consigli-per-gestire-la-quarantena-senza-stress",
                        "Quando ricevi un messaggio su Whatsapp, o vedi un post su Facebook, che riguarda il coronavirus in tono allarmistico, pensaci sempre due volte prima di condividerlo \n\nhttps://www.ilpost.it/2020/03/05/coronavirus-whatsapp-false/" ,
                        "Prova ogni sera a scrivere 2-3 cose positive della giornata, per esempio cose che ti hanno fatto stare bene oppure ringraziamenti a delle persone. Possono aiutarti a restare postivo/a \n\nhttps://www.ilpost.it/2020/03/16/consigli-psicologici-coronavirus/",
                        "Contatta un amico o amica che non senti da tempo, questa potrebbe essere un'occasione per riallacciare i rapporti \n\nhttps://www.bbc.com/news/health-51873799",
                        "Ascolta un po' di musica \n\nhttps://www.open.online/2020/03/12/coronavirus-dieci-artisti-da-ascoltare-assolutamente-durante-la-quarantena/",
                        "Inizia, o continua, a leggere un libro \n\nhttps://www.open.online/2020/03/11/coronavirus-10-libri-da-leggere-durante-la-quarantena/",
                        "Inizia una nuova serie Tv \n\nhttps://www.open.online/2020/03/13/coronavirus-dieci-serie-tv-da-vedere-assolutamente-durante-la-quarantena/",
                        "Guardati un bel film, o una serie di film \n\nhttps://www.open.online/2020/03/13/coronavirus-dieci-serie-tv-da-vedere-assolutamente-durante-la-quarantena/",
                        "Prendi una pausa dai social networks che al momento sono invasi di messaggi quasi esclusivamente legati al coronavirus \n\nhttps://www.ilpost.it/2020/03/16/consigli-psicologici-coronavirus/",
                        "Dedica del tempo a te stesso/a, così che tu possa ridurre lo stress ed evitare un burnout mentale \n\nhttps://www.bbc.com/news/health-51873799"],
                        ["https://www.bbc.com/news/health-51873799",
                         "https://www.open.online/2020/03/12/coronavirus-dieci-artisti-da-ascoltare-assolutamente-durante-la-quarantena/",
                         "https://www.open.online/2020/03/13/coronavirus-dieci-serie-tv-da-vedere-assolutamente-durante-la-quarantena/",
                         "https://www.ilpost.it/2020/03/21/quarantena-effetti-attivita-fisica/",
                         "https://www.fondazioneveronesi.it/magazine/articoli/lesperto-risponde/coronavirus-consigli-per-gestire-la-quarantena-senza-stress",
                         "https://www.ilpost.it/2020/03/16/consigli-psicologici-coronavirus/"])

fake_news_tip = TipList(["Ricordati sempre di verificare se un'informazione riguardante al Covid-19 è vera, imprecisa, decontestualizzata oppure proprio falsa",
                        "Whatsapp è un veicolo di notizie false o imprecise, che siano messaggi di testo, messaggi audio o video. Sempre verificare online prima di condividere e contribuire alla diffusione di una notizia potenzialmente dannosa",
                        "Anche Facebook è un veicolo di notizie imprecise o false riguardanti il Covid-19. Se una notizia è data in tono allarmista, allora prendila con le pinze: aspetta un'eventuale smentita, ci mette poche ore",
                        "Controlla sul web se leggi una notizia dal tono sensazionalistico, che sia Covid-19 o meno: richiede pochi click ed è alla portata di tutti",
                        "Notizie di cure miracolose date senza fonti sono raramente affidabili. Leggere che 'alcuni scienziati hanno scoperto' senza dare né nome, né università di appartenenza, né dettagli sulla cura dovrebbe far suonare un campanello di allarme"
                        ],
                        ["https://www.bufale.net/tag/covid-19/",
                        "https://www.butac.it/tag/coronavirus/",
                        "http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?lingua=italiano&id=5387&area=nuovoCoronavirus&menu=vuoto",
                        "https://www.open.online/2020/03/27/speciale-coronavirus-come-difenderti-dalle-bufale-e-i-falsi-miti-sul-covid-19/",
                        "https://www.repubblica.it/salute/medicina-e-ricerca/2020/03/20/news/coronavirus_come_nascono_la_fake_news-251764762/",
                        "https://www.ilpost.it/2020/03/05/coronavirus-whatsapp-false/",
                        "https://www.medicalfacts.it/tag/coronavirus/"])

# Loggers 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)




def tip(update, context):
    """Creates tip buttons for the users"""
    # Definisce i bottoni
    keyboard = [[InlineKeyboardButton("Esercizio fisico", callback_data='sport')],
                 [InlineKeyboardButton("Qualcosa da leggere", callback_data='books')],
                 [InlineKeyboardButton("Consiglio generico", callback_data='generic')],
                 [InlineKeyboardButton("Notizie false su Covid", callback_data='fake')]
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

    elif query.data == "generic":
        text = f"Ecco un consiglio per te per affrontare la quarantena\n\n"
        text = text + f"{generic_tip.pick_tip()}"

    elif query.data == "fake":
        text = f"Circolano molte notizie false online sul Covid-19. Anziché listartele tutte eccoti un consiglio e un articolo da leggere che riguarda le notizie false sul Covid-19\n\n"
        text = text + f"{fake_news_tip.pick_tip()}\n\n{fake_news_tip.pick_link()}"

    else:
        pass

    query.edit_message_text(text=text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
