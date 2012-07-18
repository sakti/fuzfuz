fuzfuz
======

A simple dictionary fuzzer, extendable using executor. The dictionary placed in
``data`` directory, grabbed from `fuzzdb`_.


List of Executor
----------------

- soapws
- httppost, *not complete*


Requirements
------------

For ``soapws`` executor

- `suds`_

::

    pip install suds


Usage
-----

Execute ``fuzfuz.py`` with python interpreter, FuzFuz shell will show up. Set
mandatory options, then ``run`` the executor.

::

    $ python fuzfuz.py
    FuzFuz > list
    soapws
    httppost
    FuzFuz > select soapws
    FuzFuz soapws > 

    mandatory options:
    wsdl
    method
    FuzFuz soapws > set wsdl http://example.com/ws?wsdl
    FuzFuz soapws > set method login
    FuzFuz soapws > show
    wsdl    : http://example.com/ws?wsdl
    method  : login
    FuzFuz soapws > run
    .
    .
    .
    .

    
.. _suds: https://fedorahosted.org/suds/
.. _fuzzdb: http://code.google.com/p/fuzzdb/
