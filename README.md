# 📲 WhatsApp Message Sender using Streamlit

This project is a simple **Streamlit-based desktop tool** that allows you to **send bulk WhatsApp messages** using **WhatsApp Web** — either instantly or at a scheduled time. It supports both **manual entry** and **Excel upload** for phone numbers.

---

## 🚀 Features

- 📝 Compose and send custom messages
- 📱 Enter numbers manually or upload via Excel (`PhoneNumber` column required)
- ⏰ Schedule messages to send at a specific time
- 🖥️ Opens messages in WhatsApp Web and sends using keyboard automation
- ✅ Built using Python, Streamlit, and PyAutoGUI

---

## 🖥️ How It Works

1. The user inputs a message.
2. Phone numbers can be added manually or uploaded from an Excel file.
3. The tool opens WhatsApp Web in your default browser.
4. After waiting for it to load, it automatically presses `Enter` to send the message.

---

## 📂 Installation

### 🔧 Prerequisites

- Python 3.7+
- Google Chrome or any default browser with WhatsApp Web logged in
- WhatsApp account

### 💻 Setup

```bash
git clone https://github.com/your-username/whatsapp-message-sender.git
cd whatsapp-message-sender
pip install -r requirements.txt
