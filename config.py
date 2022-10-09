from decouple import config
from dotenv import load_dotenv

load_dotenv()


class ENV:
    API_ID = config("API_ID", default=6, cast=int)
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    SESSION = config("SESSION")
