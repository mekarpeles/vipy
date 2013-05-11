#-*- coding: utf-8 -*-

"""
    vipy
    ~~~~~
    $ pip install .
"""

from distutils.core import setup
import os

setup(
    name='vipy',
    version='0.0.1',
    url='http://github.com/mekarpeles/vipy',
    author='mek',
    author_email='michael.karpeles@gmail.com',
    packages=[
        'vipy',
        ],
    platforms='any',
    license='LICENSE',
    scripts=[
        "scripts/vipy"
        ],
    description="Vipy text editor",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
)
