import os
import requests
from telegram import KeyboardButton , ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackQueryHandler,Application
from asyncio import Queue
from infrastructure.bot_handler import BotHandlers
from core.const import TOKEN


def main():
    updater = Updater(Bot(TOKEN),Queue(maxsize=0) )
    #dp = updater.dispatcher
    app= Application.builder().token(TOKEN).persistence(persistence).build()



    app.add_handler(CommandHandler("start", BotHandlers.start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, BotHandlers.button_handler))
    app.add_handler(CallbackQueryHandler(BotHandlers.button_click))


    #updater.start_polling()
    app.run_polling()
    app.idle()


if __name__ == '__main__':
    main()