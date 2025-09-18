from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext

# ==============================
# CONFIGURATION (CHANGE THESE)
# ==============================
BOT_TOKEN = "YOUR_BOT_TOKEN"       # from @BotFather
ADMIN_ID = alreadyfunde             # your Telegram ID
WALLET_ADDRESS = "YOUR_WALLET_ADDRESS"  # your USDT TRC20 wallet

# ==============================
# START COMMAND
# ==============================
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("💰 FundedNext", callback_data='fundednext')],
        [InlineKeyboardButton("📊 FundingPips", callback_data='coming')],
        [InlineKeyboardButton("🫐 Blueberry", callback_data='coming')],
        [InlineKeyboardButton("🛡 Guardia Funding", callback_data='coming')],
        [InlineKeyboardButton("⚡ Instant Funding", callback_data='coming')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("🚀 Welcome!\n\nChoose your funding option:", reply_markup=reply_markup)

# ==============================
# BUTTON HANDLER
# ==============================
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "fundednext":
        query.message.reply_text(
            "✅ Please make payment to this account:\n\n"
            f"**USDT (TRC20):** `{WALLET_ADDRESS}`\n\n"
            "📩 After payment, send me your payment proof here.\n"
            "Your message will be forwarded to the admin."
        )
    else:
        query.message.reply_text("🚧 Coming soon...")

# ==============================
# FORWARD MESSAGES TO ADMIN
# ==============================
def forward_to_admin(update: Update, context: CallbackContext):
    user = update.m
