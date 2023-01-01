from dotenv import load_dotenv
import os


dotenv_path = ".env"

if not os.path.exists(dotenv_path):
    raise Exception(f"No .env file found in '{dotenv_path}'")

load_dotenv(dotenv_path)

PROJECT_KEY = os.getenv("PROJECT_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
DATABASE_NAME = "Poems"
