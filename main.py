from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8543246126:AAEZw2SiYiCKFZhSBwDXhLwPJkPrCmMj6R0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Glory89 Bot is Online!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Available Commands:\n\n"
        "/start - Start the bot\n"
        "/help - Help Menu"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()