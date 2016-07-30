# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db.models import Q
from django.test import TestCase
from haystack.query import SearchQuerySet

from tests.testapp.models import Person
from tests.testapp.search_indexes import PersonIndex


class AutocompleteQueryTestCase(TestCase):

    fixtures = ['mock_persons']

    def setUp(self):
        PersonIndex().reindex()
        self.sqs = SearchQuerySet().all()

    def test_filter_CharField(self):
        # Make sure we only get exact hit when searching using
        # the `CharField` fields
        self.assertEqual(self.sqs.filter(firstname='abel').count(),
                         Person.objects.filter(firstname__iexact='abel').count())

        self.assertEqual(self.sqs.filter(lastname='hood').count(),
                         Person.objects.filter(lastname__iexact='hood').count())

    def test_filter_AutocompleteEdgeNgramField(self):
        # Make sure we get results for all tokens indexed using
        # the `AutocompleteEdgeNgramField`. We should get match on
        # both firstname and lastname.
        self.assertEqual(self.sqs.autocomplete(q='d').count(),
                         Person.objects.filter(Q(firstname__istartswith='d') |
                                               Q(lastname__istartswith='d')).count())

        self.assertEqual(self.sqs.autocomplete(q='ab').count(),
                         Person.objects.filter(Q(firstname__istartswith='ab') |
                                               Q(lastname__istartswith='ab')).count())

