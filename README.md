# 📞 NumGard – Telegram Phone Validator Bot

A simple and interactive **Telegram bot** built with Python that validates international phone numbers using the **NumVerify API**.

---

## 🚀 Features
- ✅ Validate international phone numbers
- 🌍 Get details like:
  - Country name & code
  - Carrier information
  - Line type (mobile, landline, etc.)
  - Geographic location (if available)
- 🧮 User limit: 5 validations per session
- 🧠 Clean and user-friendly interface
- ⚙️ Powered by [NumVerify API](https://numverify.com)

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **python-telegram-bot** (v20+)
- **Requests** (for API calls)
- **NumVerify API** (for validation)

---

## 📦 Installation

1. **Clone this repository**
   ```bash
   Install dependencies

pip install -r requirements.txt


Create a .env file (optional) and add:

API_KEY=your_numverify_api_key
BOT_TOKEN=your_telegram_bot_token


Run the bot

python main.py

⚙️ Environment Variables
Variable	Description
API_KEY	NumVerify API key from numverify.com

BOT_TOKEN	Telegram Bot token from @BotFather
📲 Usage

Start the bot with /start.

Send a phone number in international format (e.g. +14151234567 or +919876543210).

Receive a detailed validation report.

Validate up to 5 numbers per session.

🧑‍💻 Admin Contact

If you encounter issues or need more validations, contact:
👉 @encryptedgallery26

🧩 Example Output
📞 NumGard Phone Report
━━━━━━━━━━━━━━━━━━━━
🔢 Number: +14151234567
✅ Valid: Yes
🌍 Country: United States (US)
📍 Location: California
📱 Carrier: AT&T
📞 Line Type: Mobile
━━━━━━━━━━━━━━━━━━━━
🔍 Powered by NumVerify API

📚 Dependencies
python-telegram-bot>=20.0
requests


Save them in a requirements.txt file:

python-telegram-bot>=20.0
requests

🛡️ License

This project is licensed under the MIT License – feel free to modify and use it.

⭐ Credits

Developed by @encryptedgallery26(by aayush parekh)
💡 Powered by NumVerify API


---

Would you like me to generate the `requirements.txt` and `.gitignore` files for your repo too (so it’s ready to push to GitHub)?

   git clone https://github.com/yourusername/numgard-bot.git
   cd numgard-bot
