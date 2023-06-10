# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25632035"))
API_HASH = os.environ.get("API_HASH", "896d8f9929d3e00d2dae14646329fe3b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6042045034:AAEuRxIN3VMIsTuoaJXtVBZrf8EepxXHmo0")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("6094386527")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "bynklink")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://clientstamil4k:ruban9124@bynklink.mkhotjt.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6094386527")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(960432019)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001871123649")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "tamizhmasters_official") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://graph.org/file/2d88147b5a2bedc4fd35b.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
