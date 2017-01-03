from django.db import IntegrityError
from django.test import TransactionTestCase
from .models import Item


class ItemTestCase(TransactionTestCase):

    def setUp(self):
        Item.objects.create(name="Test Item")

    def test_verify_item_unique_name(self):
        """Items should always have a unique name"""
        self.assertRaises(
            IntegrityError, Item.objects.create, name="Test Item")
