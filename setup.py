#!/usr/bin/env python

from distutils.core import setup

from pipnx.__init__ import __version__

setup(name='pipnx',
      version=__version__,
      description='Python Distribution Utilities',
      author='Santacloud',
      packages=['pipnx', 'pipnx/commands',],
      scripts=['scripts/pipnx']
     )

