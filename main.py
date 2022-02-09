import praw
import os
from praw.models import Message
from dotenv import load_dotenv

def main():
    # Using a .env file to store credentials
    load_dotenv(override=True)
    CLIENT_ID = os.getenv("ID")
    CLIENT_SECRET = os.getenv("SECRET")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    reddit = praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET, 
        username = USERNAME,
        password = PASSWORD,
        user_agent = "messengerv1 by /u/"
    )

    inbox = reddit.inbox.stream()

    for message in inbox:
        if isinstance(message, Message) and not message.was_comment:
            print(f"From {message.author}: {message.body}")
            message.reply("Hi")
            # Marks the messages as read so it doesn't resend a message to the same user
            message.mark_read()

            
if __name__ == "__main__":
    main()
