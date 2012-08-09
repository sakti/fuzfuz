fuzfuz
======

A simple dictionary fuzzer, extendable using executor. The dictionary placed in
``data`` directory, grabbed from `fuzzdb`_.


List of Executor
----------------

- soapws
- httpget
- httppost, *not complete*


Requirements
------------

Python 2.6/2.7

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

License
-------

fuzfuz is released under the BSD license:

    Copyright (c) Sakti Dwi Cahyono and individual contributors.
    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

        1. Redistributions of source code must retain the above copyright notice, 
           this list of conditions and the following disclaimer.
        
        2. Redistributions in binary form must reproduce the above copyright 
           notice, this list of conditions and the following disclaimer in the
           documentation and/or other materials provided with the distribution.

        3. Neither the name of fuzfuz nor the names of its contributors may be used
           to endorse or promote products derived from this software without
           specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
    ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
    ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Future Enhancement 
-----------------

- Reporting feature
