#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="Arexa",
    description="An application that offers tenant suggestions\n
        where they should find great housing"
    "for Django.",
    version='3.2.5',
    url="https://orukopius",
    author="Oruko Pius",
    author_email="test@user.com",
    license="MIT",
    packages=find_packages(),
    install_requires=("Django>=2",),
)
