from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace with your BotFather token
TOKEN = ""

# Start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "👋 Welcome to **Silent Cheats Support Bot**!\n\n"
        "Use `/help` to see available commands. Stay safe & enjoy! 💀🔥"
    )

# Help command
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "📌 **Silent Cheats Support Bot – Commands List**\n\n"
        "✅ `/status` – Check Silent Cheats server status\n"
        "✅ `/download` – Get the latest APK link\n"
        "✅ `/setup` – Setup guide (click below)\n"
        "✅ `/support` – Contact Team Silent Cheats\n"
    )

# Status command
async def status(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "🔄 **Checking Silent Cheats server status...**\n\n"
        "🔹 Server Status: 🟢 **Online**\n"
        "🔹 Latest Update: 🔄 **Testing New Bypass**\n"
        "🔹 Estimated Maintenance End: ⏳ **Soon**\n\n"
        "Stay tuned for updates! 🚀"
    )

# Download command
async def download(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "📥 **Download Silent Cheats APK**\n\n"
        "🔥 Latest Version: **[Version Name]**\n"
        "🔗 Download Link: [Silent Cheats APK](https://shieldsister.online/silentdownload.php)\n\n"
        "⚠️ **Important:** Always follow the correct setup to avoid bans! Use `/setup` for a safe guide."
    )

# Setup command with an Inline Button
async def setup(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("🔧 Open Setup Guide", url="https://t.me/SILENTCHEATSSETUP")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "⚠️ **Follow This Setup to Avoid Ban!** ⚠️\n\n"
        "Click the button below to open the setup guide.\n",
        reply_markup=reply_markup
    )

# Support command with an Inline Button
async def support(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("🔹 Join Support Group", url="https://t.me/+n_kzk1FKI7VhMzdl")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📞 **Need Help? Contact Us!**\n\n"
        "Click below to join our **Telegram support group**:\n",
        reply_markup=reply_markup
    )

# Main function to start the bot
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("download", download))
    app.add_handler(CommandHandler("setup", setup))
    app.add_handler(CommandHandler("support", support))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
