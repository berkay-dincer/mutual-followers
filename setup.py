#!/usr/bin/env python
from setuptools import setup

VERSION = '1.0.0'
DESCRIPTION = "mutual-followers: Find out mutual friends of twitter users"
LONG_DESCRIPTION = """
mutual-followers finds out the mutual friends for given screen names. 

I use this to discover people who are tweeting about software development and also being followed by common reputable people.
"""

CLASSIFIERS = filter(None, map(str.strip,
"""
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python :: 3.7
Operating System :: OS Independent
Topic :: Utilities
Topic :: Database :: Database Engines/Servers
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))

setup(
    name="mutual-followers",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    keywords=('twitter', 'tweepy', 'friends', 'followers',
              'python', 'set'),
    author="Berkay Dincer",
    author_email="dincerbberkay@gmail.com",
    url="https://github.com/berkay-dincer/mutual-followers",
    license="MIT License",
    platforms=['any'],
    zip_safe=True,
    install_requires=['tweepy>=1.1.0', 'argparse>=1.4.0'],
    packages=['mutual-followers']
)