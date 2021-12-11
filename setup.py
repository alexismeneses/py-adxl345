#!/usr/bin/env python

from distutils.core import setup

setup(name='ADXL345',
      version='0.1',
      description='Driver for ADXL345 chip',
      author='Alexis Meneses',
      url='https://github.com/alexismeneses/py-adxl345',
      packages = ['adxl345'],
      package_dir = {'': 'lib'},
)
