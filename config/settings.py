from dotenv import load_dotenv
import os


dotenv_path = "config/.env"

if not os.path.exists(dotenv_path):
    raise Exception(f"No .env file found in '{dotenv_path}'")

load_dotenv("config/.env")

PROJECT_KEY = os.getenv("PROJECT_KEY")
DATABASE_NAME = "Poems"
