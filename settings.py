from dotenv import load_dotenv
import os


dotenv_path = ".env"

if not os.path.exists(dotenv_path):
    raise Exception(f"No .env file found in '{dotenv_path}'")

load_dotenv(dotenv_path)

PROJECT_KEY = os.getenv("PROJECT_KEY")
DATABASE_NAME = "Poems"
