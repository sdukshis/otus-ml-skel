#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='titanic',
      version='1.0',
      description='OTUS ML repo skeleton',
      author='Pavel Filonov',
      author_email='filonovpv@gail.com',
      url='https://github.com/sdukshis/otus-ml-skel',
      package_dir={"": "src"},
      packages=find_packages(where="src"),
     )