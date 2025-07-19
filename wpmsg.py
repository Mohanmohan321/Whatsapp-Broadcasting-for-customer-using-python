import streamlit as st
import pandas as pd
import webbrowser
import pyautogui
import time
import urllib.parse
from datetime import datetime

st.set_page_config(page_title="WhatsApp Sender", layout="centered")
st.title("📲 WhatsApp Message Sender")

# Message Input
message = st.text_area("📝 Enter your message:", height=150)

# Input method
method = st.radio("📥 How do you want to input numbers?", ["Manual Entry", "Upload Excel"])
phone_numbers = []

if method == "Manual Entry":
    numbers_input = st.text_area("📱 Enter numbers (comma separated with country code):", placeholder="+919876543210, +919344241894")
    if numbers_input:
        phone_numbers = [num.strip() for num in numbers_input.split(",") if num.strip()]
elif method == "Upload Excel":
    uploaded_file = st.file_uploader("📤 Upload Excel file with 'PhoneNumber' column:", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        if "PhoneNumber" in df.columns:
            phone_numbers = df["PhoneNumber"].dropna().unique().tolist()
        else:
            st.error("❌ 'PhoneNumber' column not found in uploaded file.")

# Timer setting
send_type = st.radio("⏰ When to Send?", ["Instant", "Set Timer"])
if send_type == "Set Timer":
    col1, col2 = st.columns(2)
    with col1:
        hour = st.number_input("Hour (24hr format)", 0, 23)
    with col2:
        minute = st.number_input("Minute", 0, 59)

# Send Message Logic
def send_whatsapp_msg(number, msg):
    encoded_msg = urllib.parse.quote(msg)
    url = f"https://web.whatsapp.com/send?phone={number}&text={encoded_msg}"
    webbrowser.open(url)
    time.sleep(15)  # wait for WhatsApp Web to load
    pyautogui.press("enter")
    time.sleep(5)

if st.button("🚀 Send Messages"):
    if not message.strip():
        st.warning("⚠️ Please enter a message.")
    elif not phone_numbers:
        st.warning("⚠️ Please provide at least one number.")
    else:
        st.info(f"Sending to {len(phone_numbers)} contacts...")
        for idx, number in enumerate(phone_numbers):
            try:
                if send_type == "Set Timer":
                    now = datetime.now()
                    send_time = now.replace(hour=int(hour), minute=int(minute), second=0, microsecond=0)
                    wait_sec = (send_time - now).total_seconds()
                    if wait_sec > 0:
                        st.info(f"⏳ Waiting until {send_time.strftime('%H:%M')} to send...")
                        time.sleep(wait_sec)
                send_whatsapp_msg(number, message)
                st.success(f"✅ Message sent to {number}")
            except Exception as e:
                st.error(f"❌ Failed to send to {number}: {e}")
