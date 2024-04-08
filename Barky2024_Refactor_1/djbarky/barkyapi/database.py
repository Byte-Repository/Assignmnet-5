from .models import Bookmark
from .models import Bookmark, Category

def create_bookmark(title, url, category_id, notes=None):
    """
    Function to create a new bookmark in the database.
    """
    category = Category.objects.get(id=category_id)
    bookmark = Bookmark.objects.create(title=title, url=url, category=category, notes=notes)
    return bookmark

def get_bookmarks():
    """
    Function to retrieve all bookmarks from the database.
    """
    return Bookmark.objects.all()

def get_bookmark_by_id(bookmark_id):
    """
    Function to retrieve a bookmark by its ID from the database.
    """
    return Bookmark.objects.get(id=bookmark_id)

def update_bookmark(bookmark_id, title=None, url=None, category=None, notes=None):
    """
    Function to update a bookmark in the database.
    """
    bookmark = get_bookmark_by_id(bookmark_id)
    if title:
        bookmark.title = title
    if url:
        bookmark.url = url
    if category:
        bookmark.category = category
    if notes is not None:
        bookmark.notes = notes
    bookmark.save()
    return bookmark

def delete_bookmark(bookmark_id):
    """
    Function to delete a bookmark from the database.
    """
    bookmark = get_bookmark_by_id(bookmark_id)
    bookmark.delete()
