.. image:: https://travis-ci.org/atuchak/pytest-django-cache-xdist.svg?branch=master
    :target: https://travis-ci.org/atuchak/pytest-django-cache-xdist


==========================
pytest-django-cache-xdist
==========================


A pytest-django-cache-xdist plugin for pytest

This plugin makes your django cache threadsafe by ensuring that each xdist process uses a unique cache prefix.


Installation
------------

You can install "pytest-django-cache-xdist" via `pip`_ from `PyPI`_::

    $ pip install pytest-django-cache-xdist


Usage
-----

Once installed the a fixture configures the cache settings every time pytest is run.


License
-------

Distributed under the terms of the `BSD-3`_ license.



.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
