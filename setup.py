#!/bin/env python
# -*- coding: utf8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="Nethervote",
    version=version,
    description=("Project for HackUpstate 2014 Using Flask and Evernote for "
        "Civic Hacking"),
    classifiers=[
        "Topic :: Education",
    ],
    keywords="evernote flask python civic hacking",
    author="Mike Nolan & Remy D",
    author_email="<me@michael-nolan.com> <remyd@civx.us>",
    url="http://fossrit.github.io/nethervote",
    license="AGPLv3+",
    packages=find_packages(
    ),
    scripts=[
        "distribute_setup.py",
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
        "flask-oauth",
        "evernote",
        "flask-mako",
        "feedparser",
    ],
    #TODO: Deal with entry_points
    #entry_points="""
    #[console_scripts]
    #pythong = pythong.util:parse_args
    #"""
)
