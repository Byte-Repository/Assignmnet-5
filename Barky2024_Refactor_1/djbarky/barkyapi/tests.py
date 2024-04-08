from django.test import TestCase
from .models import Category, Bookmark


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
