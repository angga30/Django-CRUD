from django.db import IntegrityError
from django.test import TransactionTestCase
from .models import Item, SubItem


class ItemTestCase(TransactionTestCase):

    def setUp(self):
        Item.objects.create(name="Test Item")

    def test_verify_item_unique_name(self):
        """Items should always have a unique name"""
        self.assertRaises(
            IntegrityError, Item.objects.create, name="Test Item")


class SubItemTestCase(TransactionTestCase):

    def setUp(self):
        self.item = Item.objects.create(name="Test Item")
        SubItem.objects.create(name="Test SubItem", item=self.item)

    def test_verify_subitem_nonunique_name(self):
        """SubItems should never need unique names"""
        SubItem.objects.create(name="Test SubItem", item=self.item)
        self.assertEqual(SubItem.objects.all().count(), 2)