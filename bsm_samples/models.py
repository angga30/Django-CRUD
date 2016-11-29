from __future__ import unicode_literals

import uuid

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from bsct.models import BSCTModelMixin


@python_2_unicode_compatible
class AbstractBase(models.Model):
    """ Abstract base model containing some useful fields """
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        blank=False, null=False, max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}: {}".format(
            self.get_class_name(),
            self.name
        )

    def get_class_name(self):
        return self.__class__.__name__


class CaseNumber(AbstractBase, BSCTModelMixin):
    """ A model Representation of a CaseNumber """

    # Many CaseNumbers can belong to a Project
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "CaseNumber"
        verbose_name_plural = "CaseNumber"


class Diagnosis(AbstractBase, BSCTModelMixin):
    """ A model Representation of a Diagnosis """
    name = models.CharField(unique=True, blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = "Diagnosis"
        verbose_name_plural = "Diagnoses"


class Project(AbstractBase, BSCTModelMixin):
    """ A model Representation of a Project """

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Sample(AbstractBase, BSCTModelMixin):
    """ A model representation of a Sample """

    ALIGNMENT_STATUS = (
        ('UNKNOWN', "Alignment status Unknown"),
        ('NEEDED', "Realignment Needed"),
        ('IN_PROGRESS', "Realignment In Progress"),
        ('COMPLETED', "Realignment Complete"),
    )
    BULK_OR_SINGLE_CELL = (
        ('BULK', "bulk"),
        ('SINGLE_CELL', "single cell"),
    )
    CNV_CALLING_STATUS = (
        ('UNKNOWN', "CNV calling status Unknown"),
        ('NEEDED', "CNV calling Needed"),
        ('IN_PROGRESS', "CNV calling In Progress"),
        ('COMPLETED', "CNV calling Complete"),
    )
    QUALITY_CHECK_STATUS = (
        ('UNKNOWN', "QC status Unknown"),
        ('NEEDED', "QC Needed"),
        ('IN_PROGRESS', "QC In Progress"),
        ('COMPLETED', "QC Complete"),
    )
    # Many Samples can belong to a CaseNumber
    alignment_status = models.CharField(
        choices=ALIGNMENT_STATUS,
        default='UNKNOWN',
        max_length=20
    )
    annotation = models.BooleanField(default=False)
    bulk_or_single_cell = models.CharField(
        choices=BULK_OR_SINGLE_CELL,
        max_length=20
    )
    case_number = models.ForeignKey('CaseNumber', on_delete=models.CASCADE)
    cnv_calling_status = models.CharField(
        choices=CNV_CALLING_STATUS,
        default='UNKNOWN',
        max_length=20
    )
    coverage = models.CharField(blank=True, null=True, max_length=250)
    date = models.DateField(auto_now=True)
    diagnosis = models.ForeignKey('Diagnosis', blank=True, null=True)
    path_to_bam = models.CharField(blank=True, null=True, max_length=250)
    path_to_raw_read = models.CharField(blank=True, null=True, max_length=250)
    path_to_vcf = models.CharField(blank=True, null=True, max_length=250)
    quality_check_status = models.CharField(
        choices=QUALITY_CHECK_STATUS,
        default='UNKNOWN',
        max_length=20
    )
    sequenced_by = models.ForeignKey(
        'SequencingCenter', blank=True, null=True)

    variant_calling = models.CharField(blank=True, null=True, max_length=250)

    class Meta:
        verbose_name = "Sample"
        verbose_name_plural = "Samples"


class SequencingCenter(AbstractBase, BSCTModelMixin):
    """ A model Representation of a SequencingCenter """

    name = models.CharField(unique=True, blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = "SequencingCenter"
        verbose_name_plural = "SequencingCenter"
