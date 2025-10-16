from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, CallbackQueryHandler, filters
import requests

API_KEY = "NumVerify API"
BOT_TOKEN = "Bot Father API"

# Dictionary to track validation count per user
user_limits = {}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_limits[user_id] = 0  # Reset on start
    welcome_text = (
        "👋 *Welcome to NumGard Bot!*\n\n"
        "🔎 Validate phone numbers using NumVerify API.\n"
        "📲 Send numbers like `+14151234567` or `+919876543210`\n\n"
        "🧪 *You can validate only 5 numbers per session.*"
        "\n━━━━━━━━━━━━━━━━━━━━━━\n"
        "ℹ️ Type /help for support"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "❓ *Help Information*\n\n"
        "👉 This bot validates international phone numbers.\n"
        "🔢 Format: `+<country_code><number>`\n"
        "🔒 Each user is allowed *only 5 validations per session*.\n\n"
        "📬 *Need help? Contact admin below:*\n"
        "[👨‍💬 @encryptedgallery26](https://t.me/encryptedgallery26)"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

# Validate number
def validate_number(number):
    url = "http://apilayer.net/api/validate"
    params = {'access_key': API_KEY, 'number': number}
    try:
        res = requests.get(url, params=params)
        return res.json()
    except Exception as e:
        return {"error": str(e)}

# Handle number messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    number = update.message.text.strip()

    # Check user limit
    count = user_limits.get(user_id, 0)
    if count >= 5:
        await update.message.reply_text("🚫 *Limit reached!*\nYou can only validate 5 numbers per session.\n\n🧑‍💻 [Contact admin](https://t.me/encryptedgallery26) for more access.", parse_mode="Markdown")
        return

    data = validate_number(number)

    if data.get("valid"):
        msg = (
            f"📞 *NumGard Phone Report*\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🔢 *Number:* `{data.get('international_format')}`\n"
            f"✅ *Valid:* `Yes`\n"
            f"🌍 *Country:* `{data.get('country_name')} ({data.get('country_code')})`\n"
            f"📍 *Location:* `{data.get('location') or 'N/A'}`\n"
            f"📱 *Carrier:* `{data.get('carrier') or 'N/A'}`\n"
            f"📞 *Line Type:* `{data.get('line_type') or 'N/A'}`\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🔍 _Powered by NumVerify API_"
        )
    elif "error" in data:
        msg = f"⚠️ *API Error:* `{data['error']}`"
    else:
        msg = "❌ *Invalid number or could not validate.*"

    user_limits[user_id] = count + 1  # Update count

    buttons = [
        [InlineKeyboardButton("🔁 Validate Another", callback_data="validate_another")],
        [InlineKeyboardButton("🌐 NumVerify", url="https://numverify.com")],
        [InlineKeyboardButton("👨‍💬 Contact Admin", url="https://t.me/encryptedgallery26")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=reply_markup)

# Handle button clicks
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "validate_another":
        await query.edit_message_text("📲 Send another phone number to validate.")

# Main runner
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_button))

    print("🤖 NumGard Bot is running...")
    app.run_polling()
