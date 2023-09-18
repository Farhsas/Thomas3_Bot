# Discord Bot with Scheduled Reminders and Memes sender

## Table of Contents
- Pre-requisites
- Getting Started
    - Installation
    - Configuration
- Bot Features
- Scheduled Reminders
- Memes sharing
- Commands
- Contributing 
- License 

## Pre-requisites
Before running this Discord bot, make sure you have the following installed:
- Python 3.x
- Discord Account
- Bot Token: You can create a bot account and get its token from the Discord Developer Portal: https://discord.com/developers/applications

## Getting Started
### Installation
1. Clone the repository
```bash
git clone https://github.com/Farhsas/Thomas3_Bot.git
```
3. Create a virtual environment and activate it:
```bash 
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
5. Insall the requirements:
```bash
pip install -r requirements.txt
```

### Configuration
1. Create a `.env` file in the root directory and add the following:
```python
TOKEN_BOT=your-bot-token-here
```
2. Customize the bot's behaviour by editing `reminder_times`, `reminder_days`, and other setting in the code as needed.

## Bot Features
### Scheduled Reminders
The bot is capable of sending scheduled reminders to a channel at specified times on specific days. It uses the following components:
- `reminder_times` - A list containing the times (in HH:MM format) at which reminders should be sent
- `reminder_days` - A list containing the days of the week (Monday, Tuesday etc.) reminders should be sent
- Functions like `break_time()`, `lunch_time()` etc. that send reminders at specific times.

### Memes sharing
The bot can share random memes from a source directory with the Discord server. It does it by randomly selcting and sending memes from the right folder (according on the time of the day). It saves the memes in another folder to avoid sending the same meme twice. But if the main folder is empty, it will randomly choose a meme inside the "used" meme folder.

### Commands
This bot primarily operates based on scheduled reonders and doesn't have user-triggered commands. However, you can extend its functionality by adding custom commands using the `discord.ext.commands` extension.

### Contributing
If you want to contribute to this project, please follow these steps:
1. Fork the repo
2. Create a new branch for your feature or bug fix
3. Make changes and test thoroughly
4. Commit changes and push them to your fork 
5. Create a pull request to the original repository

### License 
This project is licensed under the MIT License. Feel free to use, modify, and distribute it according to the terms of the license.
