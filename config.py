import os
import time

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5843311344:AAF6Waxg_DhF1tJfsyYNJ5_odUWYYh1xMNc")


    # Get from my.telegram.org (or @UseTGXBot)
    API_ID = int(os.environ.get("API_ID", "10753388"))


    # Get from my.telegram.org (or @UseTGXBot)
    API_HASH = os.environ.get("API_HASH", "bc2a8c10eada9c42315e869302c6cbc5")
    
    
    # Database URL from https://cloud.mongodb.com/
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://filter:mdisk@cluster0.t0p9ywd.mongodb.net/?retryWrites=true&w=majority")


    # Your database name from mongoDB
    DATABASE_NAME = str(os.environ.get("DATABASE_NAME", "Cluster0"))


    # ID of users that can use the bot commands
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "966029924").split())

    TIME = os.environ.get("TIME")

    # To save user details (Usefull for getting userinfo and total user counts)
    # May reduce filter capacity :(
    # Give yes or no
    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()


    # Go to https://dashboard.heroku.com/account, scroll down and press Reveal API
    # To check dyno status
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")


    # OPTIONAL - To set alternate BOT COMMANDS
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "filter")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "addgroup")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")

    ADMINS = os.environ.get("ADMINS", "966029924")

    # To record start time of bot
    BOT_START_TIME = time.time()
