from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '452386609:AAGNcVCoP39IUPWYftRcrwmQINswOvQx3_g'

def start(bot, update):
    update.message.reply_text('Goodbye!')

def hello(bot, update):
    update.message.reply_text(
        'Fuck up {}'.format(update.message.from_user.first_name))
    
def call(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text.lower()
    if text == "what's up razzy":
        bot.sendMessage(chat_id, text='Whats good my boy')
    if text == 'who do you agree with?':
        bot.sendMessage(chat_id, text='I agree with Rhaaheem, your argument is invalid!')
    


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, call))

updater.start_polling()
updater.idle()
