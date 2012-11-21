# -*- coding: utf8 -*-
from setuptools import setup
import os

pkgName = 'weakreflist'
setup(
    name=pkgName,
    version='0.1',
    url='http://www.python.org/pypi/' + pkgName,
    author='Grégory Salvan',
    author_email='apieum@gmail.com',
    license='LGPL',
    description='A WeakList class for storing objects using weak references in a list.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    package_dir={'': '.'},
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=False,
)
