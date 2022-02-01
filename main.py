import praw
import os
from praw.models import Message

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET, 
    username = USERNAME,
    password = PASSWORD,
    user_agent = ""
)

inbox = reddit.inbox.stream()


for message in inbox:
    if not message.was_comment and isinstance(message, Message):
        print(f"From {message.author}: {message.body}")
        message.reply("This is coming from an API.")
