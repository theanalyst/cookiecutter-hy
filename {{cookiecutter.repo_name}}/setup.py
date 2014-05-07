#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()

setup(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages= find_packages(exclude=['tests']),
    package_data = {
        '{{ cookiecutter.repo_name }}' : ['*.hy'],
    },
    
    install_requires=['hy >= {{ cookiecutter.hy_version }}' ],
    license= "BSD",
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 3-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        "Programming Language :: Lisp",
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
