# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.test import TestCase, override_settings
from hesab.settings import es_settings, DEFAULTS


class ESSettingsDefaultSettingsTestCase(TestCase):

    def test_default_settings(self):
        self.assertEqual(es_settings.INDEX_SETTINGS, DEFAULTS['INDEX_SETTINGS'])
        self.assertEqual(es_settings.FIELD_MAPPINGS, DEFAULTS['FIELD_MAPPINGS'])

    def test_get_invalid_setting(self):
        with self.assertRaisesMessage(AttributeError, 'Invalid Elasticsearch backend setting: \'INVALID\''):
            es_settings.INVALID


@override_settings(ES_BACKEND_SETTINGS={
    'INDEX_SETTINGS': {
        'settings': {
            'number_of_shards': 2
        }
    },
    'FIELD_MAPPINGS': 'this is just bogus'
})
class ESSettingsUserSettingsTestCase(TestCase):

    def test_user_settings(self):
        from hesab.settings import es_settings
        self.assertEqual(es_settings.INDEX_SETTINGS, {'settings': {'number_of_shards': 2}})
        self.assertEqual(es_settings.FIELD_MAPPINGS, 'this is just bogus')

