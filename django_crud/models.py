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


class Item(AbstractBase, BSCTModelMixin):
    """ A model Representation of an Item """

    name = models.CharField(unique=True, max_length=100)

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"