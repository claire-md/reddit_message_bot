import praw
from praw.models import Message

# FILE_NAME contains the path to a .txt with credential information
file = open(FILE_NAME, "r")
lines = file.readlines()

# Information must be in the same order in the .txt
CLIENT_ID = lines[0].strip()
CLIENT_SECRET = lines[1].strip()
USERNAME = lines[2].strip()
PASSWORD = lines[3].strip()

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET, 
    username = USERNAME,
    password = PASSWORD,
    user_agent = "testv1 by /u/Ok-Confection3035"
)

inbox = reddit.inbox.stream()


for message in inbox:
    if not message.was_comment and isinstance(message, Message):
        print(f"From {message.author}: {message.body}")
        message.reply("This is coming from an API.")

file.close()
