from django.db import IntegrityError
from django.test import TransactionTestCase
from .models import Diagnosis, Project, SequencingCenter


class ProjectTestCase(TransactionTestCase):

    def setUp(self):
        Project.objects.create(name="Test Project")

    def tearDown(self):
        Project.objects.all().delete()

    def test_verify_project_unique_name(self):
        """Projects should always have a unique name"""
        self.assertRaises(
            IntegrityError, Project.objects.create, name="Test Project")


class DiagnosisTestCase(TransactionTestCase):

    def setUp(self):
        Diagnosis.objects.create(name="Test Diagnosis")

    def tearDown(self):
        Diagnosis.objects.all().delete()

    def test_verify_diagnosis_unique_name(self):
        """Diagnoses should always have a unique name"""
        self.assertRaises(
            IntegrityError, Diagnosis.objects.create, name="Test Diagnosis")


class SequencingCenterTestCase(TransactionTestCase):

    def setUp(self):
        SequencingCenter.objects.create(name="Test SequencingCenter")

    def tearDown(self):
        SequencingCenter.objects.all().delete()

    def test_verify_seqcenter_unique_name(self):
        """SequencingCenters should always have a unique name"""
        self.assertRaises(
            IntegrityError, SequencingCenter.objects.create, name="Test SequencingCenter")
