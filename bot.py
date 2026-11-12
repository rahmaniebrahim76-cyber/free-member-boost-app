
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🥀 ورود به کانال شکسته‌دلان", url="https://t.me/shkeste_dellan")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "سلام دوست عزیز! 🌹\n\n"
        "به ربات افزایش ممبر رایگان خوش آمدی.\n"
        "برای آشنایی با امکانات و راهنمای استفاده، همراه ما باش.",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "برای شروع، دستور /start را بزنید."
    )

async def other_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "پیامت دریافت شد! برای شروع دستور /start را بزن."
    )

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN تنظیم نشده است.")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, other_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
