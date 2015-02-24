# -*- coding: utf-8 -*-
"""
test_confing
----------------------------------

Tests for `confing` module.
"""
import unittest
import confing
from confing import data


class TestConfing(unittest.TestCase):
  @classmethod
  def set_up(self):
    confing._confers.clear()

  def test_definition(self):
    confing.getConfer('tests').define(data.Int(name='test'))
    assert confing.getConfer('tests').load({'test': 3}).test == 3
