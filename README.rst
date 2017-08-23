url2env
=======

Turns Heroku-style database URLs into shell environment variables.

Currently only produces ``psql``-compatible envs from ``postgres://`` URLs.

Example::

    $ url2env psql://joebloggs:secret@db.example.com:4433/blog
    PGUSER=joebloggs
    PGPASSWORD=secret
    PGHOST=db.example.com
    PGPORT=4433
    PGDATABASE=blog

The output could be used in conjunction with `env`, e.g.::

    $ env $(url2env $SOME_DB_URL) psql

Installation instructions
-------------------------

::

    $ pip install url2env

Distribution instructions
-------------------------

::

    $ git tag <x.y>
    $ make dist upload
