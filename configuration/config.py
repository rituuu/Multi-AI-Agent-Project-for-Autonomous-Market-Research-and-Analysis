from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    ALLOWED_MODEL_NAMES =[
        "gemini-2.5-flash"
    ]

settings=Settings()