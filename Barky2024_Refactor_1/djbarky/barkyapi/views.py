from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from .forms import BookmarkForm
from .models import Category

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'bookmark_list.html', {'bookmarks': bookmarks})

def add_bookmark(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')
    else:
        categories = Category.objects.all()
        form = BookmarkForm(categories=categories)
    return render(request, 'add_bookmark.html', {'form': form})

def edit_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'edit_bookmark.html', {'form': form})

def delete_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        bookmark.delete()
        return redirect('bookmark_list')
    return render(request, 'delete_bookmark.html', {'bookmark': bookmark})
