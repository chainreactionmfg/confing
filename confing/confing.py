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

  def define(self, schema_node):
    assert isinstance(schema_node, colander.SchemaNode)
    if self._schema.get(schema_node.title, None) is not None:
        raise NameError(
            '%s is already defined on this Confer' % schema_node.title)
    self._schema[schema_node.title] = schema_node

  def load(self, cstruct):
    return LoadedConfig(
        self._schema.deserialize(cstruct), self._schema)


class LoadedConfig(object):
  def __init__(self, data, schema):
    self._data = data
    self._schema = schema

  def __getattr__(self, attr):
    return self[attr]

  def __getitem__(self, attr):
    data = self._data.get(attr)
    schema = self._schema[attr]
    if isinstance(schema.schema_type, colander.Mapping):
      # Nested type, so wrap it too.
      return LoadedConfig(self._data[attr], schema)
    return data

  def AsCallable(self, attr):
    return lambda: self[attr]

