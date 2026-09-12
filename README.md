# 🚀 File1Go - iLovePDF in Your Chat

[![Telegram Bot](https://img.shields.io/badge/Telegram-@file1go__bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/file1go_bot)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Render](https://img.shields.io/badge/Hosted%20on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

**File1Go** is a fast, intuitive document processing bot designed to bring powerful PDF and image editing tools directly into your favorite chat apps.

🔗 **Try it now on Telegram:** [https://t.me/file1go_bot](https://t.me/file1go_bot)

---

## 💡 Why We Built This

Popular tools like **iLovePDF** and **Smallpdf** are indispensable for handling everyday document tasks, but they usually require:
1. Opening a browser and navigating to a website.
2. Navigating through heavy web interfaces, ad popups, or login walls.
3. Manually downloading converted files to your device before re-sharing them in your chats or emails.

**File1Go was built to make an iLovePDF-like utility experience seamless and instant within chat.**

By bringing document conversion, compression, and manipulation directly to messaging platforms, users can send files, convert or compress them with interactive buttons in seconds, and forward the results immediately—no web browsers or external apps needed.

---

## ✨ Features

- 📄 **PDF ↔️ DOCX Conversion:** Convert PDF files to editable Word documents and vice versa.
- 📊 **PPTX ➡️ PDF Conversion:** Easily turn PowerPoint presentations into clean PDF documents.
- 🗜️ **PDF Compression:** Reduce PDF file sizes quickly without destroying document quality.
- 🖼️ **Image Conversions & Compression:**
  - Convert `JPG` ↔️ `PNG` with full resolution support.
  - Compress images to save storage and bandwidth.
- 🎛️ **Interactive Telegram UI:** Inline action menus tailored dynamically based on the uploaded file type.
- ⚡ **Auto-Cleanup & Security:** Uploaded files and generated conversions are processed locally and purged immediately after sending to protect user privacy.

---

## 🚀 Future Enhancements & Roadmap

We are continuously evolving File1Go to serve as the ultimate multi-platform document assistant.

- 💬 **WhatsApp Integration:** Establishing presence on WhatsApp to bring the exact same iLovePDF experience to billions of WhatsApp users worldwide.
- 🗣️ **User Feedback-Driven Updates:** Continuous feature additions based on community requests (e.g., PDF Merging, Page Splitting, Password Protection, OCR Text Extraction).
- ⚡ **Enhanced File Limits & Speed:** Multi-threaded job queuing and streaming output for ultra-fast processing of larger files.

---

## 🛠️ Project Structure

```
.
├── assets/                  # Bot branding & media assets
├── converters/              # Core conversion modules
│   ├── docx_pdf.py          # Word to PDF conversion logic
│   ├── image_compressor.py  # Image compression utilities
│   ├── image_converter.py   # Format converter (JPG/PNG)
│   ├── pdf_compressor.py    # PDF compression logic
│   ├── pdf_docx.py          # PDF to Word conversion logic
│   └── pptx_pdf.py          # PowerPoint to PDF conversion logic
├── .dockerignore
├── .env                     # Environment variables (BOT_TOKEN, PING_URL)
├── bot.py                   # Main bot logic, handlers & health check server
├── config.py                # Configuration loader
├── Dockerfile               # Production container definition
├── render.yaml              # Render deployment configuration
└── requirements.txt         # Python package dependencies
```

---

## ⚙️ Local Setup & Run

### Prerequisites
- Python 3.10 or higher
- A Telegram Bot Token (from [@BotFather](https://t.me/BotFather))

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Tele-bot-file1go.git
   cd Tele-bot-file1go
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the project root:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```

5. **Run the bot:**
   ```bash
   python bot.py
   ```

---

## 🐳 Docker & Cloud Deployment

### Docker Setup

Build and run using Docker:
```bash
docker build -t file1go-bot .
docker run -d -e BOT_TOKEN="your_token_here" --name file1go file1go-bot
```

## 🤝 Feedback & Contributions

Got feedback, feature ideas, or bug reports? We would love to hear from you! 

- Test out the live bot on Telegram: [@file1go_bot](https://t.me/file1go_bot)
- Submit an issue or open a pull request to help shape the future of File1Go!

---

Developed with ❤️ by **Kandiah**
