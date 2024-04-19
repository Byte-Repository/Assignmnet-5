# queries.py

from barkyapi.models import Bookmark

def get_all_bookmarks():
    return Bookmark.objects.all()

