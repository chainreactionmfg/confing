"""
Data descriptor API.

Currently a thin wrapper around colander.

Wrappers:
  1. Make data.Int(...) -> colander.SchemaNode(colander.Int(), ...)
  3. Make data.Range -> colander.Range
"""

import functools
import inspect

import colander


class SchemaNodeWithDoc(colander.SchemaNode):

  def Doc(self, description):
    self.description = description
    return self


def TypeWrapper(cls, *children, name, required=False, validator=None):
  # children is for nested types, like Tuple and Mapping.
  return SchemaNodeWithDoc(
      *children, typ=cls(), name=name, title=name,
      missing=required and colander.required, validator=validator)


# Patch into globals instead of doing exec('%s=%s').
g = globals()

for name, cls in colander.__dict__.items():
  # 1. data.Int -> colander.SchemaNode(colander.Int(), ...)
  if isinstance(cls, type) and issubclass(cls, colander.SchemaType):
    g[name] = functools.wraps(cls)(functools.partial(TypeWrapper, cls))
  # 2. data.Range -> colander.Range
  # Validators don't have a signature other than being callable that takes 2
  # args
  elif ((isinstance(cls, object) and hasattr(cls, '__call__')
         and len(inspect.getargspec(cls.__call__).args))
        or inspect.isfunction(cls)):
    g[name] = cls

Dict = Mapping
