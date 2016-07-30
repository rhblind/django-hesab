# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from haystack.backends.elasticsearch_backend import (
    FIELD_MAPPINGS,
    ElasticsearchSearchBackend as _ElasticsearchSearchBackend,
    ElasticsearchSearchEngine as _ElasticsearchSearchEngine
)
from hesab.settings import es_settings
from hesab.utils import merge_dict


class ElasticsearchSearchBackend(_ElasticsearchSearchBackend):
    """
    Custom Elasticsearch backend which reads configuration from the Django
    settings file.
    """

    def __init__(self, connection_alias, **connection_options):
        super(ElasticsearchSearchBackend, self).__init__(connection_alias, **connection_options)

        # Update DEFAULT_SETTINGS with custom settings
        self.DEFAULT_SETTINGS.update(**merge_dict(self.DEFAULT_SETTINGS, es_settings.INDEX_SETTINGS))

        # Update FIELD_MAPPINGS with custom field mappings
        FIELD_MAPPINGS.update(**merge_dict(FIELD_MAPPINGS, es_settings.FIELD_MAPPINGS))


class ElasticsearchSearchEngine(_ElasticsearchSearchEngine):
    backend = ElasticsearchSearchBackend

