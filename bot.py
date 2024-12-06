from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

# /start komandasiga javob beruvchi funksiya
async def start(update: Update, context):
    await update.message.reply_text("Salom! Men test botman. Testni boshlash uchun /test deb yozing.")

# /test komandasiga javob
async def test(update: Update, context):
    await update.message.reply_text("Savol: Aktivlar bu nima.")

# /help komandasiga javob
async def help(update: Update, context):
    await update.message.reply_text("Yordam: \n/start — botni boshlash uchun\n/test — testni boshlash uchun\n/help — yordam olish uchun.")

# Foydalanuvchi kiritgan xabarlarni tekshirish
async def handle_message(update: Update, context):
    text = update.message.text.lower()

    if "salom" in text:
        await update.message.reply_text("Salom! Qalaylik?")
    elif "yordam" in text:
        await update.message.reply_text("Yordam: /start — botni boshlash uchun\n/test — testni boshlash uchun")
    else:
        await update.message.reply_text("Iltimos, /start yoki /test deb yozing.")

def main():
    # Bot tokenini kiriting
    application = Application.builder().token("7551425745:AAFDzxCCDSLoJxv7S7W0rnJ-MJT6OxRnbqM").build()

    # Handlerlarni qo'shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("test", test))
    application.add_handler(CommandHandler("help", help))  # /help komandasi uchun handler
    application.add_handler(MessageHandler(filters.TEXT, handle_message))  # Xabarlar uchun handler

    # Botni ishga tushirish
    application.run_polling()

if __name__ == "__main__":
    main()
