from django.db import IntegrityError
from django.test import TestCase
from .models import Project


class ProjectTestCase(TestCase):

    def setUp(self):
        Project.objects.create(name="Test Project")

    def test_verify_unique_name(self):
        """Projects should always have a unique name"""
        self.assertRaises(
            IntegrityError, Project.objects.create, name="Test Project")
