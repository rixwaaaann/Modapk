from telegram import Update from 
telegram.ext import Application, 
CommandHandler, CallbackContext
# Replace with your actual bot token 
# from BotFather
TOKEN = 
"7503341086:AAEcW9jpUuKXtUHonMPzFNRoxJ8ur6KFO14" 
async def start(update: Update, 
context: CallbackContext):
    await 
    update.message.reply_text("Hello! 
    I'm your bot.") # ✅ Fixed
def main():
  
