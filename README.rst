Python Wrapper for Qiita API v2
===============================

Api document: http://qiita.com/api/v2/docs

Version
-------

0.1.0(2014/12/20)

Setup
-----

`qiita_v2: Python Package Index <https://pypi.python.org/pypi/qiita_v2>`_
::

  pip install qiita_v2

How to Use
----------

Simple usage
~~~~~~~~~~~~

::

  from qiita_v2.client import QiitaClient

  client = QiitaClient(access_token=<access_token>)
  res = client.get_user('petitviolet')
  res.to_json()
  # => jsonified contents


Lisence
-------

`MIT License <http://petitviolet.mit-license.org/>`_
