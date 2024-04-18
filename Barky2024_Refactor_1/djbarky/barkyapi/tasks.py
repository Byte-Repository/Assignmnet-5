from celery import shared_task
from .models import Bookmark

@shared_task
def add_bookmark_async(title, url, notes, category):
    # Create a new bookmark object with the provided data
    new_bookmark = Bookmark.objects.create(
        title=title,
        url=url,
        notes=notes,
        category=category
    )
    return new_bookmark.id  # Return the ID of the newly created bookmark

@shared_task
def edit_bookmark_async(bookmark_id, title, url, notes, category):
    # Retrieve the bookmark object to be edited
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    # Update the bookmark fields with the provided data
    bookmark.title = title
    bookmark.url = url
    bookmark.notes = notes
    bookmark.category = category
    # Save the changes to the bookmark
    bookmark.save()

@shared_task
def delete_bookmark_async(bookmark_id):
    # Retrieve the bookmark object to be deleted
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    # Delete the bookmark
    bookmark.delete()
