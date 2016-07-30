# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.test import TestCase
from hesab.utils import merge_dict


class MergeDictTestCase(TestCase):

    def setUp(self):
        self.dict_a = {
            'firstname': 'Chuck',
            'skills': {
                'karate': {
                    'proficiency': 5,
                }
            },
            'buddies': []
        }
        self.dict_b = {
            'lastname': 'Norris',
            'skills': {
                'karate': {
                    'favorite trick': 'Roundhouse Kick',
                    'proficiency': 10
                }
            },
            'buddies': [
                'James Trivette',
                'Captain C.D. Parker'
            ]
        }

    def test_merge_dict(self):
        expected = {
            'buddies': [
                'James Trivette',
                'Captain C.D. Parker'
            ],
            'firstname': 'Chuck',
            'lastname': 'Norris',
            'skills': {
                'karate': {
                    'favorite trick': 'Roundhouse Kick',
                    'proficiency': 10
                }
            }
        }
        self.assertDictEqual(merge_dict(self.dict_a, self.dict_b), expected)

    def test_merge_dict_non_valid(self):
        args = [
            {'a': [], 'b': {}},
            {'a': {}, 'b': []},
            {'a': '', 'b': {}},
            {'a': 10, 'b': {}},
            {'a': {}, 'b': 10},
            {'a': True, 'b': {}},
        ]
        for arg in args:
            try:
                merge_dict(arg['a'], arg['b'])
            except TypeError as e:
                self.assertEqual(str(e), 'Invalid type. Expected dict object.')
                continue
