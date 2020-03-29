---
noteId: "97a8072071cc11eabf979522b255bfd9"
tags: []

---

# Quaran-Tips
A Telegram bot with some tips and activities to preserve your mental health during quarantine periods.

Un bot di Telegram con suggerimenti e attività per preservare lo stato mentale di una persona durante il periodo di quarantena.
Piccolo progetto per l'hackaton [Hack@Home](https://hackatho.me/) per l'emergenza COVID-19.

La salute mentale è importante per le persone e, anche se piccolo, questo è il nostro contributo.

---

## Cosa fa il bot?

Quaran-Tips fornisce all'utente alcuni piccoli servizi per il benessere durante la quarantena.

- Primo tra tutti il bot funziona come un diario personale, il bot suggerisce all'utente di inserire 2-3 pensieri positivi così da liberarsi la mente da tutta la negatività che la pandemia sta creando. L'utente, quando vuole, può ri-leggere tutti i pensieri sia uno alla volta, sia tutti insieme.

- Il bot fornisce un promemoria che può essere attivato (e disattivato) per ricordare all'utente di inserire i pensieri positivi.

- Infine, il bot può dare qualche consiglio su come affrontare la quarantena, linkando anche qualche articolo di giornale interessante da leggere.

## Comandi

Digitare i seguenti comandi per far eseguire un'azione al bot: 

- ``/start``: Mostra il messaggio di benvenuto e crea il diario
- ``/help``: Fornisce le informazioni necessarie per usare il bot
- ``/tip``: Il bot fornisce alcune categorie che l'utente può selezionare per ricevere un consiglio
- ``/pensiero``: Scrivi un pensiero insieme a questo comando per aggiungerlo al tuo diario
- ``/listapensieri``: Mostra tutti i pensieri scritti
- ``/pensierorandom``: Mostra un pensiero casuale
- ``/promemoriagiornaliero``: Crea un promemoria che quotidianamente ti invia un consiglio per la quarantena 
- ``/cancellapromemoria``: Cancella il promemoria

---

## Developer guide

This bot has been developed with the python-telegram-bot API ([link](https://github.com/python-telegram-bot/python-telegram-bot)).

### Requirements

- Python 3

Install all the required packages with ``pip install -r requirements.txt``

### Usage

To run a bot you need first to get an API token from the botfather. See [here](https://core.telegram.org/bots#6-botfather) how.
We use a json file called ``token.json`` storing our token. You can use any other method: be sure to change the code to fetch the token in the ``bot.py`` script.

- bot.py is the starting point of the bot
- run an instance of the bot with ``python bot.py``

---

## Autori

Andrea Bachechi - [B4k3](https://github.com/B4k3)

Chiara Baraglia - [CB-92](https://github.com/CB-92)

Luca Di Mauro - [dima91](https://github.com/dima91)

Andrea Lisi - [0Alic](https://github.com/0Alic)

\#andràtuttobene :rainbow: