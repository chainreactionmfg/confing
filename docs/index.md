# Confing does configuration right.

Configuration defining and loading. The hard part of configuration isn't
reading file formats anymore, it's managing it across a large (or even small)
codebase.

The API is modeled after the `logging` module to avoid collisions, however no
inheritance is enabled.

## Getting started

Install via pip: `pip install confing`

## Defining
In your module, define a configuration key you want to use.

```python
import confing
from confing import data

confer = confing.getConfer('my_module')
confer.define(
    data.Int(name='key_name', validator=data.Range(0, 10)).doc(
        textwrap.dedent(
            '''
            The documentation of this configuration key. Can be read later
            by iterating through the defined keys of a confer object.
            ''')))

confer.define(data.Dict(
    data.Int(name='first').doc('Children can also be documented.'),
    data.String(name='second').doc(
        "Don't let your future developers ask what this key is for."),
    name='').doc('And you can expose this to your sysadmins, end users, etc!'))
```

Then you can include it in your config data like so:

```yaml
key_name: 5
```

## Loading

And you can load it easily. Notice we don't handle the actual format, in this
case yaml. Just load it into python objects first.

```python
loaded_config = confer.load(yaml.load(file_obj))
loaded_config.key_name == 5
```

