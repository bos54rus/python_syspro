from setuptools import setup, Extension

module = Extension('foreign', sources=['foreign.c'])

setup(name='foreign',
      version='1.0',
      description='Module for matrix power calculation',
      ext_modules=[module])
