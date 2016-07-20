# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from haystack import indexes


class AutocompleteEdgeNgramField(indexes.EdgeNgramField):
    """
    Custom field for doing autocomplete searches.
    """
    field_type = 'autocomplete_edge_ngram'
