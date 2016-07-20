# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.test import TestCase
from haystack import connections
from haystack.backends.elasticsearch_backend import FIELD_MAPPINGS


class ElasticsearchSearchBackendTestCase(TestCase):
    """
    Make sure the ElasticsearchSearchBackend is initialized with updated
    settings.
    """

    def test_backend_default_settings(self):
        # Make sure the backend DEFAULT_SETTINGS has received
        # the default custom settings
        backend = connections['default'].get_backend()

        # The default elasticsearch backend ships with two analyzers;
        # the "ngram_analyzer" and the "edgengram_analyzer". Make sure the "autocomplete_analyzer"
        # is appended.
        for analyzer in ('ngram_analyzer', 'edgengram_analyzer', 'autocomplete_analyzer'):
            self.assertIn(analyzer,
                          backend.DEFAULT_SETTINGS['settings']['analysis']['analyzer'])

    def test_field_mapping(self):
        # Make sure the custom field mapping is patched in place
        self.assertIn('autocomplete_edge_ngram', FIELD_MAPPINGS)
