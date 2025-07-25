<p align="center">
  <img src="https://files.catbox.moe/5j4gmj.jpg" alt="AutoFeedback Logo" width="500px">
</p>

<h1 align="center">🤖 AutoFeedback Bot</h1>

<p align="center">
  <b>A Telegram Bot that automatically forwards all messages to a specified channel for feedback or logging.</b>
</p>

<p align="center">
  <a href="https://t.me/KomalBotsNetwork"><img src="https://img.shields.io/badge/Update%20Channel-blue?style=for-the-badge&logo=telegram&logoColor=white" alt="Update Channel"></a>
  <a href="https://t.me/KomalMusicRobotSupport"><img src="https://img.shields.io/badge/Support%20Group-blue?style=for-the-badge&logo=telegram&logoColor=white" alt="Support Group"></a>
  <a href="https://t.me/ItsKapilYadav"><img src="https://img.shields.io/badge/Owner-KapilYadav-purple?style=for-the-badge&logo=telegram&logoColor=white" alt="Owner"></a>
</p>

<p align="center">
  <a href="https://github.com/RockMusicBot/Autofeedback-/fork"><img src="https://img.shields.io/github/forks/RockMusicBot/Autofeedback-?style=social" alt="GitHub Forks"></a>
  <a href="https://github.com/RockMusicBot/Autofeedback-/stargazers"><img src="https://img.shields.io/github/stars/RockMusicBot/Autofeedback-?style=social" alt="GitHub Stars"></a>
</p>

<p align="center">
<a href="https://dashboard.heroku.com/new?template=https://github.com/RockMusicBot/Autofeedback-"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-purple?style=for-the-badge&logo=heroku&logoColor=white" width="250px" alt="Deploy to Heroku"></a>
</p>

---

## 📌 What Is AutoFeedback Bot?

**AutoFeedback** is a minimal and powerful Telegram bot designed to **automatically forward all received messages** (including media, text, and other content) to a **designated channel** for feedback collection, moderation, logging, or storage.

This bot is especially useful for:
- Collecting user feedback anonymously
- Centralizing private messages for admin review
- Logging messages from private groups/chats

---

## 🚀 Features

- ✅ Automatically forwards every message
- ✅ Supports text, photo, videos, stickers, voice, and more
- ✅ Admin-only command to set or change the target channel
- ✅ Lightweight and minimal dependencies
- ✅ Supports Heroku, Render, and VPS deployment

---

## 🛠️ Deployment

### 🔧 VPS Installation

```bash
# Update packages
sudo apt update && sudo apt upgrade -y


# Clone the repo
git clone https://github.com/RockMusicBot/Autofeedback-.git
cd Autofeedback-

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt

# Configure your environment variables (edit .env or config.py)
