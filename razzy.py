from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '452386609:AAGNcVCoP39IUPWYftRcrwmQINswOvQx3_g'

def start(bot, update):
    update.message.reply_text('Goodbye!')

def hello(bot, update):
    update.message.reply_text(
        'Fuck up {}'.format(update.message.from_user.first_name))
    
def cosign(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    if text == 'Aye Razzy':
        bot.sendMessage(chat_id, text='Whats good my boy')


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, cosign))



updater.start_polling()
updater.idle()
