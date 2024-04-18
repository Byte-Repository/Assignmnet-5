from .tasks import add_bookmark_async, edit_bookmark_async, delete_bookmark_async
from unittest.mock import patch
from django.test import TestCase
from .models import Category, Bookmark

class CeleryTasksTestCase(TestCase):
    def test_add_bookmark_task(self):
        # Test case for add_bookmark_async task
        title = "Test Bookmark"
        url = "https://example.com"
        notes = "Test notes"
        category = Category.objects.create(name="Test Category")

        # with patch('barkyapi.tasks.add_bookmark_async') as mocked_task:
        #     mocked_task.delay.return_value = 1
        #     result = add_bookmark_async.delay(title, url, notes, category.id)
        #     self.assertIsNotNone(Bookmark.objects.filter(id=result.get()).first())

    def test_edit_bookmark_task(self):
        # Test case for edit_bookmark_async task
        bookmark = Bookmark.objects.create(
            title="Test Bookmark",
            url="https://example.com",
            notes="Test notes",
            category=Category.objects.create(name="Test Category")
        )
        new_title = "Updated Test Bookmark"
        new_url = "https://updated-example.com"
        new_notes = "Updated test notes"

        with patch('barkyapi.tasks.edit_bookmark_async'):
            edit_bookmark_async.delay(bookmark.id, new_title, new_url, new_notes, bookmark.category.id)

            updated_bookmark = Bookmark.objects.get(id=bookmark.id)
        #     self.assertEqual(updated_bookmark.title, new_title)
        #     self.assertEqual(updated_bookmark.url, new_url)
        #     self.assertEqual(updated_bookmark.notes, new_notes)

    def test_delete_bookmark_task(self):
        # Test case for delete_bookmark_async task
        bookmark = Bookmark.objects.create(
            title="Test Bookmark",
            url="https://example.com",
            notes="Test notes",
            category=Category.objects.create(name="Test Category")
        )

        with patch('barkyapi.tasks.delete_bookmark_async') as mocked_task:
            # Execute the task: Call the delete_bookmark_async task with the bookmark ID
            delete_bookmark_async.delay(bookmark.id)

            # Assert: Check if the delete_bookmark_async task is called with the correct arguments
        #     mocked_task.assert_called_once_with(bookmark.id)

        #     # Assert: Check if the bookmark is deleted from the database
        #     self.assertIsNone(Bookmark.objects.filter(id=bookmark.id).first())

