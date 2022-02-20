import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings 
import ephem
from datetime import date


logger = logging.getLogger(__name__)

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
         'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

current_date = date.today()

planets = {'Mars': ephem.Mars(current_date), 'Venus': ephem.Venus(current_date), 'Saturn': ephem.Saturn(current_date), 'Jupiter': ephem.Jupiter(current_date),
               'Neptune': ephem.Neptune(current_date), 'Uranus': ephem.Uranus(current_date), 'Mercury': ephem.Mercury(current_date)}
def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Hello! How you doin?')


def talk_to_me(update, context):
    user_text = update.message.text
    logger.info(user_text)
    update.message.reply_text(user_text)

def name_planet(update, context):
    print('Вызван /planet')
    update.message.reply_text('Which planet do you choose?')
    which_planet= update.message.text.split()[1]
    user_planet = planets.get(which_planet, None)
    if user_planet!= None:
        constellation = ephem.constellation(planets[which_planet])
        update.message.reply_text(constellation[1])
    else:
        update.message.reply_text('Whaaaat?!')

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", name_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logger.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
