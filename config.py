# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "15415755"))
API_HASH = os.environ.get("API_HASH", "dc4f9540457541bc4de6e4bfb630db71")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6240570615:AAG11PFpf7s7W72_aHKS3jCbBc-HWcmuus4")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("15415755")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Grolink")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://yash8833:OXZ1lnADF1s0qaO0@cluster0.6r2rrdp.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "15415755")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1782059495)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-938960731")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Grolink_Official_Channel") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://i.ibb.co/XVydpmt/IMG-20230528-215336-407.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
