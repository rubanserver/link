# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25632035"))
API_HASH = os.environ.get("API_HASH", "896d8f9929d3e00d2dae14646329fe3b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6033859982:AAFRGI-GW9m9InFh-YXBaXkD881ctQBxThg")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("6094386527")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "rubanlink")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://clientstamil4k:basker123@cluster0.9aoaypf.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6094386527")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(960432019)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001959062681")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "tamil4katmos") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://i.ibb.co/XVydpmt/IMG-20230528-215336-407.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
