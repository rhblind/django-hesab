# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from haystack import indexes
from tests.testapp.models import Person
from hesab.fields import AutocompleteEdgeNgramField


class PersonIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=False)
    firstname = indexes.CharField(model_attr='firstname')
    lastname = indexes.CharField(model_attr='lastname')
    q = AutocompleteEdgeNgramField()

    @staticmethod
    def prepare_q(obj):
        tokens = ' '.join((obj.firstname, obj.lastname))
        return ' '.join(set(tokens.split()))

    def get_model(self):
        return Person

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
