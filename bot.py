from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from datetime import datetime
import os

# Load environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # Must be an integer

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to the Feedback Bot!\nUse /feedback <your message> to share your thoughts.\nUse /help to view commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 *Available Commands:*\n"
        "/start - Start message\n"
        "/feedback <message> - Send feedback\n"
        "/help - Show this help\n\n"
        "📎 You can also send media (photos/videos/files) to forward to admin.",
        parse_mode="Markdown"
    )

async def handle_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Use: `/feedback your message`", parse_mode="Markdown")
        return

    feedback_text = ' '.join(context.args)
    sender = update.effective_user
    chat_type = update.effective_chat.type
    sender_name = sender.full_name
    username = f"@{sender.username}" if sender.username else "No username"
    time_sent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = (
        f"📩 *New Feedback Received!*\n"
        f"👤 *From:* {sender_name} ({username})\n"
        f"💬 *Chat Type:* {chat_type}\n"
        f"🕒 *Time:* `{time_sent}`\n\n"
        f"💬 *Feedback:*\n{feedback_text}"
    )

    await context.bot.send_message(chat_id=CHANNEL_ID, text=message, parse_mode='Markdown')
    await update.message.reply_text("✅ Feedback sent!")

async def handle_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sender = update.effective_user
    chat_type = update.effective_chat.type
    sender_name = sender.full_name
    username = f"@{sender.username}" if sender.username else "No username"
    time_sent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    caption = (
        f"📩 *New Media Feedback!*\n"
        f"👤 *From:* {sender_name} ({username})\n"
        f"💬 *Chat Type:* {chat_type}\n"
        f"🕒 *Time:* `{time_sent}`\n\n"
        f"🖼️ Media attached."
    )

    if update.message.photo:
        await context.bot.send_photo(chat_id=CHANNEL_ID, photo=update.message.photo[-1].file_id, caption=caption, parse_mode='Markdown')
    elif update.message.document:
        await context.bot.send_document(chat_id=CHANNEL_ID, document=update.message.document.file_id, caption=caption, parse_mode='Markdown')
    elif update.message.video:
        await context.bot.send_video(chat_id=CHANNEL_ID, video=update.message.video.file_id, caption=caption, parse_mode='Markdown')

    await update.message.reply_text("✅ Media forwarded!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("feedback", handle_feedback))

    media_filter = filters.PHOTO | filters.VIDEO | filters.Document.ALL
    app.add_handler(MessageHandler(media_filter, handle_media))

    print("🤖 Feedback Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
