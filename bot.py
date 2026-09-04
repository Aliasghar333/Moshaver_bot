import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👨‍🏫 پنل مشاور", callback_data="advisor")],
        [InlineKeyboardButton("👨‍🎓 پنل دانش‌آموز", callback_data="student")],
    ]

    await update.message.reply_text(
        "🎓 به سامانه مشاوران خوش آمدید.\n\n"
        "لطفاً گزینه موردنظر را انتخاب کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "advisor":
        await query.edit_message_text(
            "👨‍🏫 پنل مشاور\n\n"
            "این بخش در حال ساخت است."
        )

    elif query.data == "student":
        await query.edit_message_text(
            "👨‍🎓 پنل دانش‌آموز\n\n"
            "این بخش در حال ساخت است."
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
