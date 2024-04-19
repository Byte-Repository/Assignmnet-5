# handlers.py

from utils.commands import create_bookmark_command
from .handlers import create_bookmark_handler


def create_bookmark_handler(title, url):
    # Call the create_bookmark_command function to create a new bookmark
    # You can implement the actual logic here, such as validation and saving to the database
    return create_bookmark_command(title, url)
