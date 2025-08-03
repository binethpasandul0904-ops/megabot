from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 හෙලෝ! Video එකක් එවන්න. Mama link eka denna.")

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video or update.message.document
    if not video:
        await update.message.reply_text("📎 කරුණාකර video file එකක් එවන්න.")
        return
    file = await context.bot.get_file(video.file_id)
    await update.message.reply_text(f"📥 Direct link: {file.file_path}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.VIDEO | filters.Document.ALL, handle_video))

app.run_polling()
