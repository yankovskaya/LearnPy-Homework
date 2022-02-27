import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
from datetime import datetime

dt_now = datetime.now()
current_date = dt_now.strftime('%d/%m/%Y')

planet_dict = {'Mars': ephem.Mars(current_date), 'Venus': ephem.Venus(current_date), 'Saturn': ephem.Saturn(current_date), 'Jupiter': ephem.Jupiter(current_date),
               'Neptune': ephem.Neptune(current_date), 'Uranus': ephem.Uranus(current_date), 'Mercury': ephem.Mercury(current_date)}

logger = logging.getLogger(__name__)

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
         'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Hello! How you doin?')


def talk_to_me(update, context):
    user_text = update.message.text
    logger.info(user_text)
    update.message.reply_text(user_text)

def name_planet(update, context):
    print('Вызван /planet')
    user_txt = update.message.text.split()[1]
    user_planet = planet_dict.get(user_txt, None)
    if not user_planet:
        update.message.reply_text("Whaaat?")
    if user_planet == True:
        constellation = ephem.constellation(user_planet)
        update.message.reply_text(f'Constellathion: {constellation[1]}')



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