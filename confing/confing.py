"""
Configuration defining and loading.
"""
import colander
from confing import data

_confers = {}


def getConfer(name):
  confer = _confers.get(name)
  if confer:
    return confer
  confer = Confer(name)
  _confers[name] = confer
  return confer


class Confer(object):

  def __init__(self, name):
    self._name = name
    self._schema = colander.Schema()
    self._loaded = None

  def define(self, schema_node):
    assert isinstance(schema_node, colander.SchemaNode)
    if self._schema.get(schema_node.title, None) is not None:
        raise NameError(
            '%s is already defined on this Confer' % schema_node.title)
    self._schema[schema_node.title] = schema_node

  @property
  def definitions(self):
    return self._schema.children

  def load(self, cstruct):
    if self._loaded is not None:
      raise ValueError('Cannot load the same config twice.')
    self._loaded = LoadedConfig(
        self._schema.deserialize(cstruct), self._schema)
    return self._loaded

  @property
  def loaded(self):
    return self._loaded

  def AsCallable(self, attr):
    def ConfigCallable():
      if self._loaded is None:
        raise ValueError('Config is not loaded yet.')
      return self._loaded[attr]
    return ConfigCallable


class LoadedConfig(object):
  def __init__(self, data, schema):
    self._data = data
    self._schema = schema

  def __getattr__(self, attr):
    return self[attr]

  def __getitem__(self, attr):
    data = self._data.get(attr)
    schema = self._schema[attr]
    if isinstance(schema.typ, colander.Mapping):
      # Nested type, so wrap it too.
      return LoadedConfig(self._data[attr], schema)
    return data
