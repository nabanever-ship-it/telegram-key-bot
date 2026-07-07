from telegram import Update

2 from telegram.ext import Application, CommandHandler, ContextTypes

3

4 BOT_TOKEN =

"8543246126: AAEZw2SiYiCKFZhSBwDXhLwPJkPrCmMj6R0"

5

6 async def start(update: Update, context: ContextTypes. DEFAULT_TYPE):

await update.message.reply_text( 7

"✔ Glory89 Bot is Online!")

8

9 async def help_command(update: Update, context:

ContextTypes.DEFAULT_TYPE):

await update.message.reply_text(

59%

:

10

11

"Available Commands: \n"

12

"/start Start the bot\n"

13

"/help Help Menu"

14 )

15

16 def main():

17 app Application.builder().token (BOT_TOKEN).build()

18

19

app.add_handler (CommandHandler("start", start))

20 app.add_handler (CommandHandler("help", help_command))

21

22 print("Bot Started...")

23

app.run_polling()

24

25 if __name__ == "__main__":

26

main()