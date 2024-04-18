from celery import shared_task
from .models import Bookmark

@shared_task
def add_bookmark_async(title, url, notes, category):
    return Bookmark.objects.create(title=title, url=url, notes=notes, category=category).id

@shared_task
def edit_bookmark_async(bookmark_id, title, url, notes, category):
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    bookmark.title, bookmark.url, bookmark.notes, bookmark.category = title, url, notes, category
    bookmark.save()

@shared_task
def delete_bookmark_async(bookmark_id):
    Bookmark.objects.get(pk=bookmark_id).delete()
