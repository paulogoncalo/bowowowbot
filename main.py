import telegram
import configparser

from telegram.ext import Updater, CommandHandler

# Configuring bot
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

def bowowow(bot, update):
    try:

        msg = "BOW"
        # Send the message with menu
        bot.send_message(chat_id=update.message.chat_id,
                        text=msg)
        msg = "OWOWOW"
        bot.send_message(chat_id=update.message.chat_id,
                        text=msg)
        msg = "OWOW"
        bot.send_message(chat_id=update.message.chat_id,
                        text=msg)
        msg = "OWOWOW"
        bot.send_message(chat_id=update.message.chat_id,
                        text=msg)
        msg = "OW"
        bot.send_message(chat_id=update.message.chat_id,
                        text=msg)
        msg = "OWOWOWOW"
        bot.send_message(chat_id=update.message.chat_id,
                        text=msg)
        msg = "OWOWOW"
        bot.send_message(chat_id=update.message.chat_id,
                        text=msg)
        msg = "OW"
        bot.send_message(chat_id=update.message.chat_id,
                        text=msg)

    except Exception as e:
        print(e)

def main():

    updater = Updater(token=config['DEFAULT']['token'])
    dispatcher = updater.dispatcher

    bowowow_handler = CommandHandler('bowowow', bowowow)
    dispatcher.add_handler(bowowow_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()

