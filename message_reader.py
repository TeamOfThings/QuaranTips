from database import engine, Thought
from datetime import datetime
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

def message_handler(update, context):
    session = Session()
    user_says = " ".join(context.args)
    user_id = update.message.from_user.id
    date = update.message.date
    try:
        thought = Thought(text=user_says, author_id=user_id, date=date)
        session.add(thought)
        session.commit()
    except Exception as e:
        print(e)
    #update.message.reply_text("Il tuo messaggio è stato salvato")
    reply =  str(user_id) + " : " + str(user_says)
    update.message.reply_text(reply)


def date_to_string(uxdate):
    ts = int(uxdate)
    # if you encounter a "year is out of range" error the timestamp
    # may be in milliseconds, try `ts /= 1000` in that case
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M')