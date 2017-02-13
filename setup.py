#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='lyrically',
    version='1.0',
    description='Parser for the Lyrically Wikia (lyrics.wikia.com)',
    author='Wingysam',
    url='',
    packages=['lyrically'],
    requires=['dryscrape', 'bs4']
)
