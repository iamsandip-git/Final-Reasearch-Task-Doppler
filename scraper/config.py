from dotenv import load_dotenv

import os


load_dotenv()

ekantipur_categories = [
    "business",
    "news",
    "opinion",
    "sports",
    "national",
    "entertainment",
    "feature",
    "world",
    "blog",
    "koseli",
    "diaspora",
    "Education",
    "photo_feature",
]

db_config = {
    "dbname": os.getenv("DATABASE_NAME"),
    "user": os.getenv("DATABASE_USERNAME"),
    "password": os.getenv("DATABASE_PASSWORD"),
    "host": os.getenv("DATABASE_HOST"),
    "port": os.getenv("DATABASE_PORT"),
}
