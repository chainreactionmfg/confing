#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Based on https://github.com/pypa/sampleproject/blob/master/setup.py."""
# To use a consistent encoding
from codecs import open
import os
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from setuptools.command.test import test
import sys

# Shortcut for building/publishing to Pypi
if sys.argv[-1] == 'publish':
  os.system('python setup.py sdist bdist_wheel upload')
  sys.exit()


class pytest(test):
    user_options = [
        ('pytest-args=', None, "Arguments to pass to py.test"),
        ('pytest-cov=', None, "Enable coverage. Choose output type: "
         "term, html, xml, annotate, or multiple with comma separation"),
    ]

    def initialize_options(self):
        test.initialize_options(self)
        self.pytest_args = 'tests'
        self.pytest_cov = None

    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run(self):
        import pytest
        cov = ''
        if self.pytest_cov is not None:
            outputs = ' '.join('--cov-report %s' % output
                               for output in self.pytest_cov.split(','))
            cov = ' --cov confing ' + outputs
        sys.exit(pytest.main(self.pytest_args + cov))

# Get the long description from the relevant file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

with open(os.path.join(here, 'requirements.txt')) as req:
  requires = [line.strip().decode('ascii') for line in req.readlines()]

setup(
    name='confing',
    version='0.1.0',
    description='Described configuration for large, complex projects',
    long_description=long_description,
    keywords='confing development',
    author='Fahrzin Hemmati',
    author_email='fahhem@chainreactionmfg.com',
    license='Apache 2.0',
    url='https://github.com/fahhem/confing',
    packages=find_packages(exclude=('tests*', 'docs')),
    include_package_data=True,
    package_data={
        '': ['README.md', 'LICENSE', 'AUTHORS'],
    },
    install_requires=requires,
    tests_require=[
        'pytest',
    ],
    cmdclass=dict(
        test=pytest,
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
)
