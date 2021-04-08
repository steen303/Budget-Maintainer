from unittest import TestCase
from domain.category import Category


class TestCategory(TestCase):
    def setUp(self):
        self.category1 = Category(1, "Category 1")
        self.category2 = Category(2, "Category 2")
        self.category3 = Category(3, "Category 3")

    def test_change_name(self):
        self.assertEqual(self.category1.name, "Category 1", "Category 1 is named wrong")
        self.assertEqual(self.category2.name, "Category 2", "Category 2 is named wrong")
        self.assertEqual(self.category3.name, "Category 3", "Category 3 is named wrong")
        self.category3.name = "Cat 3"
        self.assertEqual(self.category3.name, "Cat 3", "Category 3 is named wrong")

    def test_get_json(self):
        self.assertEqual(self.category1.get_json(), {"id": 1, "name": "Category 1"}, "JSON incorrect")

    def test_get_json(self):
        self.assertEqual(self.category2.get_json(), {"id": 2, "name": "Category 2"}, "JSON incorrect")


class TestCategories(TestCase):
    def test_add_categorie(self):
        self.fail()

    def test_get_categories_json(self):
        self.fail()
