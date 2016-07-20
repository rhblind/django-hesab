# -*- coding: utf-8 -*-
"""
Settings for the Elasticsearch backend are all namespaced in
the ES_BACKEND_SETTINGS setting. For example:

ES_BACKEND_SETTINGS = {
    'INDEX_SETTINGS': {
        'settings': {
            'number_of_shards': 2
        }
    },
    'FIELD_MAPPINGS': {
        ...
    }
}
"""

from __future__ import unicode_literals

from django.conf import settings
from django.core.signals import setting_changed


DEFAULTS = {
    'INDEX_SETTINGS': {
        'settings': {
            'number_of_shards': 1,
            'analysis': {
                # Analyzer and filter for making autocomplete work
                # like expected with Elasticsearch.
                'analyzer': {
                    'autocomplete_analyzer': {
                        'type': 'custom',
                        'tokenizer': 'standard',
                        'filter': [
                            'lowercase',
                            'autocomplete_filter'
                        ]
                    }
                },
                'filter': {
                    'autocomplete_filter': {
                        'type': 'edgeNGram',
                        'min_gram': 1,
                        'max_gram': 20
                    }
                }
            }
        }
    },
    'FIELD_MAPPINGS': {
        'autocomplete_edge_ngram': {
            'type': 'string',
            'index_analyzer': 'autocomplete_analyzer',
            'search_analyzer': 'standard'
        }
    }
}


class ESSettings(object):

    def __init__(self, user_settings=None, defaults=None):
        self._user_settings = user_settings
        self.defaults = defaults or DEFAULTS

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError('Invalid Elasticsearch backend setting: \'%s\'' % attr)

        try:
            value = self.user_settings[attr]
        except KeyError:
            value = self.defaults[attr]

        # Cache the setting
        setattr(self, attr, value)
        return value

    @property
    def user_settings(self):
        if not getattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'ES_BACKEND_SETTINGS', {})
        return self._user_settings

es_settings = ESSettings(None, DEFAULTS)


def reload_es_settings(*args, **kwargs):
    global es_settings
    setting, value = kwargs['setting'], kwargs['value']
    if setting == 'ES_BACKEND_SETTINGS':
        es_settings = ESSettings(value, DEFAULTS)

setting_changed.connect(reload_es_settings)
