# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in solarkitchen/__init__.py
from solarkitchen import __version__ as version

setup(
	name='solarkitchen',
	version=version,
	description='Solar kitchen food reservation',
	author='kinisi e-mobility',
	author_email='vasanth@kinisi.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
