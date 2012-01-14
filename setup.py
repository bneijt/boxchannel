import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "boxchannel",
    version = "0.0.1",
    author = "A. Bram Neijt",
    author_email = "bneijt@gmail.com",
    description = ("An attempt to communicate blocks over a fixed size shared directory."),
    license = "GPLv3",
    url = "https://github.com/bneijt/boxchannel",
    packages=['boxchannel', 'tests'],
    long_description=read('README.md'),
    install_requires=[
        'mmh3',
        'simplejson',
    ],
)
