from telegram.ext import Updater, CommandHandler

# Define a function that will handle the /start command
def start(update, context):
    # Send a message back when the /start command is issued
    update.message.reply_text("Hello! I am your Telegram bot. How can I assist you today?")

# Define a function that will handle the /help command
def help_command(update, context):
    # Send a help message
    update.message.reply_text("You can control me by sending these commands:\n/start - Start the bot\n/help - Get help")

# Main function to start the bot
def main():
    # Replace 'YOUR_API_TOKEN' with your actual bot token from BotFather
    TOKEN = "7729338094:AAH0-e-bVHjOA_V-ykT6z9i1BfFiamchhuo"
    
    # Create an Updater object with the bot token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register handlers for the /start and /help commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Start the bot
    updater.start_polling()

    # Keep the bot running until interrupted
    updater.idle()

if __name__ == '__main__':
    main()
