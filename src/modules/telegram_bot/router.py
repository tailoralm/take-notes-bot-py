import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from photo import handle_photo
from document import handle_document
from video import handle_video
from voice import handle_voice
from text import handle_text


class Router:
    def __init__(self):
        token = os.getenv('TELEGRAM_TOKEN')
        if not token:
            raise ValueError("Telegram bot token not found in environment variables.")

        self.bot = Application.builder().token(token).build()

        self.bot.add_handler(MessageHandler(filters.ALL, self.check_authorization), group=0)

        self.bot.add_handler(MessageHandler(filters.Document.ALL, handle_document))
        self.bot.add_handler(MessageHandler(filters.Document.ALL, handle_photo))
        self.bot.add_handler(MessageHandler(filters.Document.ALL, handle_video))
        self.bot.add_handler(MessageHandler(filters.Document.ALL, handle_voice))
        self.bot.add_handler(MessageHandler(filters.Document.ALL, handle_text))

        self.commands()
        self.bot.run_polling()

    def commands(self):
        help_handler = CommandHandler('help', self.help_command)
        self.bot.add_handler(help_handler)

        start_handler = CommandHandler('start', self.start_command)
        self.bot.add_handler(start_handler)

    @staticmethod
    async def help_command(update: Update):
        await update.message.reply_text(
            'To save something, add the command in the caption or reply with the command.'
        )

    @staticmethod
    async def start_command(update: Update):
        first_name = update.message.from_user.first_name
        await update.message.reply_text(f'Hello, {first_name}! Welcome to the bot.')

    @staticmethod
    async def check_authorization(update: Update, context: ContextTypes.DEFAULT_TYPE, next_handler):
        my_telegram_id = os.getenv('MY_TELEGRAM_ID')
        if not my_telegram_id:
            await update.message.reply_text(f'Your chat ID: {update.message.from_user.id}')
            return

        if update.message.from_user.id != int(my_telegram_id):
            await update.message.reply_text('Not Authorized')
            return

        await next_handler(update, context)
