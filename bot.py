import os
import random
import discord
import datetime
import asyncio
from PIL import Image
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN_BOT")


intents = discord.Intents.default()
intents.typing = False  # Disable typing events to reduce unnecessary traffic
intents.presences = False  # Disable presence events for the same reason

bot = commands.Bot(command_prefix="!", intents=intents)


reminder_times = ["08:55", "11:00", "12:30", "13:25", "15:00", "16:55", "15:47"]
reminder_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
trainees = [
    "Alemash",
    "Alexandra",
    "Alexandre",
    "Camillo",
    "Joseph",
    "Nicolas Delhem",
    "Matthias",
    "Nicolas Deneubourg",
    "Zian Cattoul",
    "Volodymir",
    "Anthony",
    "Gilles",
    "Michael",
    "Loic",
    "Thomas",
    "Julien",
    "Thu Hong",
    "Jeoffrey",
    "Pavlo",
    "Macit",
    "Louise",
    "Akberet",
    "Philippe",
]
break_memes = "/Users/ziancattoul/Desktop/Thomas3_Bot/Thomas3_Bot/break_memes"
break_memes_used = "/Users/ziancattoul/Desktop/Thomas3_Bot/Thomas3_Bot/break_memes_used"
lunch_memes = "Thomas3_Bot/lunch_memes"
lunch_memes_used = "Thomas3_Bot/lunch_memes_used"


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await schedule_reminders()


async def memes_sender(source_dir, destination_dir):
    try:
        image_file = [
            f
            for f in os.listdir(source_dir)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp"))
        ]

        if image_file:
            random_meme = random.choice(image_file)

            source_path = os.path.join(source_dir, random_meme)
            destination_path = os.path.join(destination_dir, random_meme)

            meme_image = Image.open(source_path)

            with open(source_path, "rb") as f:
                for guild in bot.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "général":
                            meme = discord.File(f)
                            await channel.send(file=meme)

            meme_image.save(destination_path)

            os.remove(source_path)

        if not image_file:
            image_file = [
                f
                for f in os.listdir(destination_dir)
                if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp"))
            ]

            random_meme = random.choice(image_file)

            destination_path = os.path.join(destination_dir, random_meme)

            with open(destination_path, "rb") as f:
                for guild in bot.guilds:
                    for channel in guild.text_channels:
                        if channel.name == "général":
                            meme = discord.File(f)
                            await channel.send(file=meme)

    except Exception as er:
        print(f"An error occured: {str(er)}")


async def break_time():
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.name == "général":
                await channel.send(f"Break Time!")
                await memes_sender(break_memes, break_memes_used)


async def lunch_time():
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.name == "général":
                await channel.send(f"Lunch Time! Don't forget to clock!")
                await memes_sender(break_memes, break_memes_used)


async def clock_reminder():
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.name == "clock":
                await channel.send(f"Don't forget to clock")
                # await memes_sender(break_memes, break_memes_used)


async def end_day():
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.name == "général":
                cleaners = random.sample(trainees, 2)
                await channel.send(
                    f"Don't forget to clock!{cleaners[0]} and {cleaners[1]}, it's your turn to clean the coffee machines. Thank You!"
                )


async def schedule_reminders():
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        current_day = datetime.datetime.now().strftime("%A")

        if current_day in reminder_days:
            if current_time in reminder_times:
                if current_time == "11:00" or current_time == "15:00":
                    await break_time()

                elif current_time == "12:30":
                    await lunch_time()

                elif current_time == "16:55" or current_time == "16:30":
                    if current_day == "Wednesday" or current_day == "Friday":
                        await clock_reminder()
                    else:
                        await end_day()

                else:
                    await clock_reminder()

        # Sleep for 1 minute before checking again (adjust as needed)
        await asyncio.sleep(60)


bot.run(TOKEN)
