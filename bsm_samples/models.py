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
        blank=False, null=False, unique=True, max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}".format(
            self.name
        )


class SequencingCenter(BSCTModelMixin, AbstractBase):
    """ A model Representation of a Sequencing Center """
    class Meta:
        verbose_name = "SequencingCenter"
        verbose_name_plural = "SequencingCenters"


class Project(BSCTModelMixin, AbstractBase):
    """ A model Representation of a project done at a sequencing center """

    # Many Projects can belong to a SequencingCenter
    sequencing_center = models.ForeignKey(
        'SequencingCenter', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Sample(BSCTModelMixin, AbstractBase):
    """ A model representation of a biological sample """

    ALIGNMENT_STATUS = (
        ('UNKNOWN', "Alignment status Unknown"),
        ('NEEDED', "Realignment Needed"),
        ('IN_PROGRESS', "Realignment In Progress"),
        ('COMPLETED', "Realignment Complete")
    )

    # Many Samples can belong to a Project
    project = models.ForeignKey(
        'Project', blank=True, null=True, on_delete=models.CASCADE)

    case_number = models.IntegerField(blank=False, null=False)
    bulk = models.BooleanField(default=False)
    single_cell = models.BooleanField(default=False)
    quality_check_status = models.BooleanField(default=False)
    annotation = models.BooleanField(default=False)
    path_to_bam = models.CharField(blank=False, null=False, max_length=250)
    path_to_raw_read = models.CharField(
        blank=False, null=False, max_length=250)
    path_to_vcf = models.CharField(blank=False, null=False, max_length=250)

    # Could the following 4 use a set of choices like alignment_status ???
    diagnosis = models.CharField(blank=False, null=False, max_length=250)
    coverage = models.CharField(blank=False, null=False, max_length=250)
    variant_calling = models.CharField(blank=False, null=False, max_length=250)
    cnv_calling = models.CharField(blank=False, null=False, max_length=250)

    alignment_status = models.CharField(
        choices=ALIGNMENT_STATUS,
        default='UNKNOWN',
        max_length=50
    )

    class Meta:
        verbose_name = "Sample"
        verbose_name_plural = "Samples"
