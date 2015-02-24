# confing
[![Build Status](https://img.shields.io/travis/chainreactionmfg/confing/master.svg)](https://travis-ci.org/chainreactionmfg/confing)
[![Coverage Status](https://img.shields.io/coveralls/chainreactionmfg/confing/master.svg)](https://coveralls.io/r/chainreactionmfg/confing)
[![Documentation Status](https://readthedocs.org/projects/confing/badge/?version=latest&style=flat)](https://readthedocs.org/projects/confing/?badge=latest)
[![PyPI Version](https://img.shields.io/pypi/v/confing.svg)](https://pypi.python.org/pypi/confing)
[![PyPI License](https://img.shields.io/pypi/l/confing.svg)](https://pypi.python.org/pypi/confing)

Described configuration for large, complex projects.
[Read the docs!](http://confing.readthedocs.org/en/latest/)

## Features

* Define config keys using a nicer API to colander.
* Get config values as a callable before loading or directly afterwards.
* Define multiple 'confers' to allow large codebases to be worked on independently.


## Quick Usage

Firstly, define the key(s) you want to be in the config file. They can be any
type colander supports, even custom types. Builtin types can be accessed more
easily through the included `data` module.

```python
import confing
from confing import data

confer = confing.getConfer('my_confer_name')
confer.define(data.String(name='secret_key'))
```

Next, load the data for the configuration.

```python
loaded = confer.load({'secret_key': '...'})
loaded is confer.loaded
```

Lastly, get the key you want out of the config.

```python
confer.loaded.secret_key
# or
confer.loaded['secret_key']
```

If you need to pass a configuration value to something either at module-import
time or before the config is loaded, you can pass it a callable that will be
the correct value once the config is loaded later. This will only work if the
receiving party doesn't attempt to resolve the value before the config is loaded.

``python
confer.as_callable('secret_key')
```


## Install for development
```bash
$ pip install --editable .
```


## Contributing
Anyone can help make this project better - read [CONTRIBUTION](CONTRIBUTION.md) to get started!


## License
Apache 2.0. See the [LICENSE](LICENSE) file for more details.

