from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Your BotFather API token and your personal Telegram Chat ID
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
MY_CHAT_ID = "YOUR_PERSONAL_CHAT_ID" # You can get this from @userinfobot

# A function to handle the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["FundedNex"],
        ["FundingPips", "Blueberry"],
        ["Instant Funding", "Guardia Funding"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome! Please select an option below:",
        reply_markup=reply_markup
    )

# A function to handle button presses
async def handle_button_press(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    if user_message == "FundedNex":
        response_text = "Please pay to this crypto account: [Your Account Details Here]\n\nThen, reply to me and let me know, and your message will be forwarded to the admin."
        await update.message.reply_text(response_text)
    else:
        await update.message.reply_text("Coming soon! This service is not yet available.")

# A function to forward user messages to you
async def forward_message_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_chat_id = update.message.chat_id
    # Get the user's name
    user_info = update.message.from_user.first_name
    
    # Construct the message to be sent to you
    forwarded_message = f"**New message from a user!**\n\n**User:** {user_info} (ID: {user_chat_id})\n\n**Message:**\n{update.message.text}"
    
    # Forward the message to your personal chat ID
    await context.bot.send_message(chat_id=MY_CHAT_ID, text=forwarded_message)

# Main function to run the bot
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Register the command and message handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_button_press))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message_to_admin))

    application.run_polling()

if __name__ == "__main__":
    main()
