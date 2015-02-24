# -*- coding: utf-8 -*-
"""
test_confing
----------------------------------

Tests for `confing` module.
"""
import unittest

import colander

from confing import confing
from confing import data


class TestConfing(unittest.TestCase):
  @classmethod
  def setUp(self):
    confing._confers.clear()

  def test_definition(self):
    confing.getConfer('tests').define(data.Int(name='test'))
    assert confing.getConfer('tests').load({'test': 3}).test == 3

  def test_repetitions(self):
    confer = confing.getConfer('tests')

    # Repeat definition.
    confer.define(data.Int(name='test'))
    with self.assertRaises(NameError):
      confer.define(data.Int(name='test'))

    # Repeat load.
    confer.load({'test': 1})
    with self.assertRaises(ValueError):
      confer.load({'test': 2})

  def test_doccing(self):
    confer = confing.getConfer('tests')
    confer.define(data.Int(name='with_doc').Doc('Just a test int'))
    for defn in confer.definitions:
      print(defn, defn.__dict__)
      assert defn.description == 'Just a test int'

  def test_callable(self):
    confer = confing.getConfer('tests')
    confer.define(data.Int(name='with_doc').Doc('Just a test int'))
    callable = confer.as_callable('with_doc')

    with self.assertRaises(ValueError):
      callable()

    confer.load({'with_doc': 5})
    assert callable() == 5

  def test_nested(self):
    confer = confing.getConfer('tests')
    confer.define(data.Dict(
        data.Int(name='first', required=True),
        data.String(name='second'),
        name='dict', required=True))
    with self.assertRaises(colander.Invalid):
      confer.load({})
    with self.assertRaises(colander.Invalid):
      confer.load({'dict': {'second': 'text'}})
    confer.load({'dict': {'first': 3, 'second': 'text'}})
    assert confer.loaded.dict.first == 3
