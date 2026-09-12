import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    CommandHandler
)
from telegram.utils.request import Request
from config import BOT_TOKEN

from converters.pdf_docx import convert_pdf_to_docx
from converters.docx_pdf import convert_docx_to_pdf
from converters.pptx_pdf import convert_pptx_to_pdf
from converters.image_converter import convert_image
from converters.image_compressor import compress_image
from converters.pdf_compressor import compress_pdf
import time
TEMP_DIR = "temp"

if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

# Store user files temporarily
user_files = {}


# 0️⃣ Start Command
def start(update, context):
    welcome_text = (
        "Hi file1Go, built by Ck\n\n"
        "I am capable of:\n"
        "• Converting PDF to DOCX\n"
        "• Compressing PDFs\n"
        "• Converting Images (JPG ↔️ PNG)\n"
        "• Converting DOCX/PPTX to PDF\n\n"
        "Upload files and see the magic ✨"
    )
    
    # Path to the welcome image
    image_path = os.path.join("assets", "welcome_bot_image.png")
    
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            update.message.reply_photo(photo=f, caption=welcome_text)
    else:
        update.message.reply_text(welcome_text)


# 1️⃣ Handle file upload
def handle_file(update, context):
    if update.message.document:
        document = update.message.document
        file_name = document.file_name
        file = document.get_file()

    elif update.message.photo:
        photo = update.message.photo[-1]  # highest resolution
        file = photo.get_file()
        file_name = f"{photo.file_unique_id}.jpg"

    else:
        update.message.reply_text("Unsupported file type.")
        return

    file_path = os.path.join(TEMP_DIR, file_name)
    file.download(file_path)
    name, ext = os.path.splitext(file_name)
    ext = ext.lower()

    user_id = update.message.from_user.id
    user_files[user_id] = file_path

    keyboard = []

    if ext == ".pdf":
        keyboard = [
            [InlineKeyboardButton("PDF → DOCX", callback_data="pdf_to_docx")],
            [InlineKeyboardButton("Compress PDF", callback_data="compress_pdf")]
        ]

    elif ext == ".docx":
        keyboard = [
            [InlineKeyboardButton("DOCX → PDF", callback_data="docx_to_pdf")]
        ]

    elif ext == ".pptx":
        keyboard = [
            [InlineKeyboardButton("PPTX → PDF", callback_data="pptx_to_pdf")]
        ]

    elif ext == ".jpg":
        keyboard = [
            [InlineKeyboardButton("JPG → PNG", callback_data="jpg_to_png")],
            [InlineKeyboardButton("Compress Image", callback_data="compress_image")]
        ]

    elif ext == ".png":
        keyboard = [
            [InlineKeyboardButton("PNG → JPG", callback_data="png_to_jpg")],
            [InlineKeyboardButton("Compress Image", callback_data="compress_image")]
        ]

    else:
        update.message.reply_text("Unsupported file type.")
        return

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Select what you want to do:",
        reply_markup=reply_markup
    )


# 2️⃣ Handle button clicks
def handle_button(update, context):
    query = update.callback_query
    try:
        query.answer()
        query.edit_message_text("🚀 Hold tight! Magic is happening... ⏳")
    except Exception:
        pass

    user_id = query.from_user.id

    if user_id not in user_files:
        query.edit_message_text("❌ File expired or not found. Please upload again.")
        return

    input_path = user_files[user_id]
    name, ext = os.path.splitext(input_path)
    output_path = None

    try:
        if query.data == "pdf_to_docx":
            output_path = name + ".docx"
            convert_pdf_to_docx(input_path, output_path)

        elif query.data == "compress_pdf":
            output_path = name + "_compressed.pdf"
            compress_pdf(input_path, output_path)

        elif query.data == "docx_to_pdf":
            output_path = name + ".pdf"
            convert_docx_to_pdf(input_path, output_path)

        elif query.data == "pptx_to_pdf":
            output_path = name + ".pdf"
            convert_pptx_to_pdf(input_path, output_path)

        elif query.data == "jpg_to_png":
            output_path = name + ".png"
            convert_image(input_path, output_path)

        elif query.data == "png_to_jpg":
            output_path = name + ".jpg"
            convert_image(input_path, output_path)

        elif query.data == "compress_image":
            output_path = name + "_compressed.jpg"
            compress_image(input_path, output_path)

        query.edit_message_text("✅ Done! Sending your file now... 📤")
        
        time.sleep(1) # Small buffer
        with open(output_path, "rb") as f:
            context.bot.send_document(
                chat_id=query.message.chat_id,
                document=f,
                timeout=120
            )

    except Exception as e:
        query.edit_message_text(f"⚠️ Oops! Something went wrong: {e}")

    finally:
        # Cleanup: Delete both input and output files
        if os.path.exists(input_path):
            os.remove(input_path)
        if output_path and os.path.exists(output_path):
            os.remove(output_path)
        
        # Remove from user_files tracking
        if user_id in user_files:
            del user_files[user_id]


import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK - Bot is active!")

    def log_message(self, format, *args):
        return  # Silence HTTP logs

def start_health_check_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    print(f"Health check server running on port {port}...")
    server.serve_forever()

import urllib.request

def self_ping():
    ping_url = os.environ.get("PING_URL") or os.environ.get("RENDER_EXTERNAL_URL")
    if not ping_url:
        print("Self-ping disabled: Neither PING_URL nor RENDER_EXTERNAL_URL is configured.")
        print("Tip: Add PING_URL=https://tele-bot-file1go.onrender.com to Render Environment Variables.")
        return

    if not ping_url.startswith("http://") and not ping_url.startswith("https://"):
        ping_url = "https://" + ping_url

    print(f"Self-ping active for target: {ping_url}")
    while True:
        time.sleep(720)  # Ping every 12 minutes (720 seconds)
        try:
            req = urllib.request.Request(ping_url, headers={"User-Agent": "Render-Self-Ping/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                print(f"[Self-Ping] Ping sent to {ping_url} - Status: {resp.status}")
        except Exception as e:
            print(f"[Self-Ping] Failed to ping {ping_url}: {e}")

def main():
    # Start HTTP server thread so Render detects a valid Web Service on Free Tier ($0/mo)
    threading.Thread(target=start_health_check_server, daemon=True).start()

    # Start Self-Ping thread to ping every 12 minutes
    threading.Thread(target=self_ping, daemon=True).start()

    request = Request(
        connect_timeout=60,
        read_timeout=60
    )

    updater = Updater(
        token=BOT_TOKEN,
        request_kwargs={
            "connect_timeout": 60,
            "read_timeout": 60
        },
        use_context=True
    )

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.document | Filters.photo, handle_file))

    dp.add_handler(CallbackQueryHandler(handle_button, run_async=True))

    updater.start_polling()
    print("Bot running with UI mode...")
    updater.idle()
if __name__ == "__main__":
    main()

