#!/usr/bin/env python

#from distutils.core import setup, find_packages
from setuptools import setup, find_packages

import dropbox_index


setup(
    name='dropbox-index',
    version=dropbox_index.__version__,
    author="Wojciech 'KosciaK' Pietrzok, bspkrs",
    author_email='kosciak@kosciak.net, bspkrs@gmail.com',
    description='Creates index.html for directory contents shared publicly on Dropbox. That way you can easily share whole content of the directory without the need to send separate links for all the shared files',
    long_description='Visit project\s page for details.',
    url='https://github.com/bspkrs/dropbox-index',
    license='Apache License v2',
    keywords='dropbox',
    classifiers=[
        "Development Status :: 5 - Beta",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ],
    packages=find_packages(exclude=['ez_setup', 
                                    'tests', 'tests.*'
                                    'examples', 'examples.*']),
    entry_points={
        'console_scripts': [
            'dropbox-index = dropbox_index:run',
        ],
    },
    #scripts = ['bin/dropbox-index'],
)

