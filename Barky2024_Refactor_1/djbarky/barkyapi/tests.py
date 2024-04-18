from django.test import TestCase
from .models import Category, Bookmark
from .tasks import add_bookmark_async, edit_bookmark_async, delete_bookmark_async
from unittest.mock import patch, MagicMock
import unittest

class CategoryModelTests(TestCase):
    def test_category_creation(self):
        # Create a category
        category = Category.objects.create(name="Test Category")

        # Check if the category was created successfully
        self.assertEqual(category.name, "Test Category")


class BookmarkModelTests(TestCase):
    def test_bookmark_creation(self):
        # Create a category
        category = Category.objects.create(name="Test Category")

        # Create a bookmark associated with the category
        bookmark = Bookmark.objects.create(
            title="Test Bookmark",
            url="https://example.com",
            category=category
        )

        # Check if the bookmark was created successfully
        self.assertEqual(bookmark.title, "Test Bookmark")
        self.assertEqual(bookmark.url, "https://example.com")
        self.assertEqual(bookmark.category, category)

class CeleryTasksTestCase(TestCase):
    def test_add_bookmark_task(self):
        # Test case for add_bookmark_async task
        # Define test scenario: Create a new bookmark and check if it's added successfully
        title = "Test Bookmark"
        url = "https://example.com"
        notes = "Test notes"
        category = Category.objects.create(name="Test Category")

        # Mock the call to add_bookmark_async
        with patch('barkyapi.tasks.add_bookmark_async') as mocked_task:
            mocked_task.delay.return_value = MagicMock(get=lambda: 1)
            # Execute the task: Call the add_bookmark_async task with test data
            result = add_bookmark_async.delay(title, url, notes, category.id)

            # Assert: Check if the bookmark is created in the database
            self.assertIsNotNone(Bookmark.objects.filter(id=result.get()).first())

    def test_edit_bookmark_task(self):
        # Test case for edit_bookmark_async task
        # Define test scenario: Edit an existing bookmark and check if it's updated successfully
        bookmark = Bookmark.objects.create(
            title="Test Bookmark",
            url="https://example.com",
            notes="Test notes",
            category=Category.objects.create(name="Test Category")
        )
        new_title = "Updated Test Bookmark"
        new_url = "https://updated-example.com"
        new_notes = "Updated test notes"

        # Mock the call to edit_bookmark_async
        with patch('barkyapi.tasks.edit_bookmark_async') as mocked_task:
            # Execute the task: Call the edit_bookmark_async task with test data
            edit_bookmark_async.delay(bookmark.id, new_title, new_url, new_notes, bookmark.category.id)

            # Assert: Check if the bookmark is updated in the database
            updated_bookmark = Bookmark.objects.get(id=bookmark.id)
            self.assertEqual(updated_bookmark.title, new_title)
            self.assertEqual(updated_bookmark.url, new_url)
            self.assertEqual(updated_bookmark.notes, new_notes)

    def test_delete_bookmark_task(self):
        # Test case for delete_bookmark_async task
        # Define test scenario: Delete an existing bookmark and check if it's removed successfully
        bookmark = Bookmark.objects.create(
            title="Test Bookmark",
            url="https://example.com",
            notes="Test notes",
            category=Category.objects.create(name="Test Category")
        )

        # Mock the call to delete_bookmark_async
        with patch('barkyapi.tasks.delete_bookmark_async') as mocked_task:
            # Execute the task: Call the delete_bookmark_async task with the bookmark ID
            delete_bookmark_async.delay(bookmark.id)

            # Assert: Check if the bookmark is deleted from the database
            self.assertIsNone(Bookmark.objects.filter(id=bookmark.id).first())

# Additional test cases for other Celery tasks can be added here

if __name__ == "__main__":
    # Run the tests
    unittest.main()
