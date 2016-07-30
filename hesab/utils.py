# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from copy import deepcopy
from django.utils import six


def merge_dict(a, b):
    """
    Recursively merges and returns dict a with dict b.
    :param a: dictionary object
    :param b: dictionary object
    :return: merged dictionary object
    """

    if not isinstance(a, dict) or not isinstance(b, dict):
        raise TypeError('Invalid type. Expected dict object.')

    result = deepcopy(a)
    for key, val in six.iteritems(b):
        if key in result and isinstance(result[key], dict):
            result[key] = merge_dict(result[key], val)
        else:
            result[key] = deepcopy(val)

    return result
