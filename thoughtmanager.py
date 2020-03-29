from database import engine, Thought
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import random


class ThoughtManager:

    def __init__(self):
        self.session = None
        self.Session = sessionmaker(bind=engine)

    def thought_handler(self, update, context):
        self.session = self.Session()
        user_says = " ".join(context.args)
        user_id = update.message.from_user.id
        date = update.message.date
        try:
            thought = Thought(text=user_says, author_id=user_id, date=date)
            self.session.add(thought)
            self.session.commit()
        except Exception as e:
            print(e)
        #update.message.reply_text("Il tuo messaggio è stato salvato")
        reply = self.date_to_string(date) + " : " + str(user_id) + " : " + str(user_says)
        update.message.reply_text(reply)

    
    def get_thoughts_list(self, update, context):
        self.session = self.Session()
        user_id = update.message.from_user.id
        try:
            reply = "Ecco un lista dei pensieri positivi che hai inserito finora!\n\n"
            t_list = self.session.query(Thought).filter(Thought.author_id == user_id).order_by(Thought.date)
            prec_date = None
            for t in t_list:
                curr_date = self.date_to_string(t.date)
                if prec_date != None and prec_date == curr_date :
                    reply = reply + "[" + self.date_to_hours(t.date) + "] - " + t.text + "\n\n"
                else:
                    reply = reply + self.date_to_string(t.date) +":\n\n" + "["+ self.date_to_hours(t.date) + "] - " + t.text + "\n\n"
                prec_date = curr_date        
            update.message.reply_text(reply)
        except Exception as e:
            print(e)

    def get_random_though(self, update, context):
        self.session = self.Session()
        user_id = update.message.from_user.id
        rand = random.randrange(0, self.session.query(Thought).count()-1) 
        row = self.session.query(Thought).filter(Thought.author_id == user_id)[rand]
        update.message.reply_text("Il giorno " + self.date_to_string(row.date) +" alle ore " + self.date_to_hours(row.date) + " hai scritto: \""+ row.text +"\"")
        

    def date_to_string(self, uxdate):
        month_array = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']

        month_num = int(uxdate.strftime('%m'))
        day_num = uxdate.strftime('%d')
        year_num = uxdate.strftime('%Y')
        
        return day_num + ' ' + month_array[month_num - 1] + ' ' + year_num

    def date_to_hours(self, uxdate):
        return uxdate.strftime(' %H:%M ')