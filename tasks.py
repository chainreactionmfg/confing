#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from invoke import run, task
from invoke.util import log, enable_logging
enable_logging()


@task
def test():
  """test - run the test runner."""
  run('python setup.py test', pty=True)


@task(name='test-all')
def testall():
  """test-all - run tests on every Python version with tox."""
  run('tox')


@task
def clean():
  """clean - remove build artifacts."""
  run('rm -rf build/')
  run('rm -rf dist/')
  run('rm -rf confing.egg-info')
  run('find . -name *.pyc -delete')
  run('find . -name *.pyo -delete')
  run('find . -name *~ -delete')
  run('find . -name __pycache__ -delete')

  log.info('cleaned up')


@task
def lint():
  """lint - check style with flake8."""
  run('flake8 confing tests')


@task
def coverage():
  """coverage - check code coverage quickly with the default Python."""
  run('python setup.py test --pytest-cov=html')
  run('open htmlcov/index.html')

  log.info('collected test coverage stats')


@task(clean)
def start_publish():
  """start_publish - package a release for the cheeseshop."""
  run('python setup.py sdist bdist_wheel', pty=True)
  log.info('Packaged release 0.1.1')


@task(clean)
def finish_publish():
  """publish - upload the release to the cheeseshop."""
  run('twine upload dist/confing-0.1.1*')
  log.info('published new release')
