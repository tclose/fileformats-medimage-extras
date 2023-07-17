FileFormats-CHANGEME Extras
===========================
.. image:: https://github.com/arcanaframework/fileformats-CHANGEME-extras/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/arcanaframework/fileformats-CHANGEME-extras/actions/workflows/tests.yml
.. image:: https://codecov.io/gh/arcanaframework/fileformats-CHANGEME-extras/branch/main/graph/badge.svg?token=UIS0OGPST7
    :target: https://codecov.io/gh/arcanaframework/fileformats-CHANGEME-extras
.. image:: https://img.shields.io/github/stars/ArcanaFramework/fileformats-CHANGEME-extras.svg
    :alt: GitHub stars
    :target: https://github.com/ArcanaFramework/fileformats-CHANGEME
.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat
    :target: https://arcanaframework.github.io/fileformats/
    :alt: Documentation Status


How to customise this template
------------------------------

#. Name your repository with the name fileformats-<SUBPACKAGE-TO-ADD-EXTRAS-TO>-extras
#. Rename the `fileformats/extras/CHANGEME` directory to the name of the fileformats subpackage the extras are for
#. Search and replace "CHANGEME" with the name of the fileformats subpackage the extras are to be added
#. Replace name + email placeholders in `pyproject.toml` for developers and maintainers
#. Implement selected "extras" by implementing functions decorated by one of the ``*_extra`` hooks defined in the target fileformats class
#. Ensure that the decorated are imported into the extras package root, i.e. `fileformats/extra/CHANGEME`
#. Delete these instructions


...


This is a extras module for the
[fileformats-CHANGEME](https://github.com/ArcanaFramework/fileformats-CHANGEME) package, which provides
additional functionality to format classes (i.e. aside from basic identification and validation), such as
conversion tools, metadata parsers, test data generators, etc...


Quick Installation
------------------

This extension can be installed for Python 3 using *pip*::

    $ pip3 install fileformats-CHANGEME-extras

This will install the core package and any other dependencies

License
-------

This work is licensed under a
`Creative Commons Attribution 4.0 International License <http://creativecommons.org/licenses/by/4.0/>`_

.. image:: https://i.creativecommons.org/l/by/4.0/88x31.png
  :target: http://creativecommons.org/licenses/by/4.0/
  :alt: Creative Commons Attribution 4.0 International License
