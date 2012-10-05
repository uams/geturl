#!/usr/bin/env python

from distutils.core import setup

setup(name='geturl',
    version='0.2.1',
    description='A CLI tool to get a public link for any file',
    author='uams',
    license="MIT",
    url='https://github.com/uams/geturl',
    scripts=['geturl'],
    py_modules=['check_output'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 3 - Beta",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ]

)
