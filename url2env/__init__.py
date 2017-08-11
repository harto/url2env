#!/usr/bin/env python3

"""
Transforms Heroku-style database URLs into shell environment variables.
"""

from os.path import basename
from sys import argv
from urllib.parse import urlparse

def psql_envs(conn):
    env_map = {'user': 'PGUSER',
               'pass': 'PGPASSWORD',
               'host': 'PGHOST',
               'port': 'PGPORT',
               'db': 'PGDATABASE'}
    return dict((env_map[k], v) for k, v in conn.items() if v)

def to_envs(url):
    assert url.scheme in ('postgresql', 'postgres', 'psql'), \
        'unsupported URL scheme: %s' % url.scheme
    conn = {'user': url.username,
            'pass': url.password,
            'host': url.hostname,
            'port': url.port,
            'db': url.path[1:]}
    return psql_envs(conn)

def format_envs(envs):
    return '\n'.join('%s=%s' % (k, v) for k, v in envs.items())

def main():
    try:
        url = argv[1]
    except IndexError:
        _exit_with_usage()
    print(format_envs(to_envs(urlparse(url))))

def _exit_with_usage():
    print('usage: %s <url>' % basename(argv[0]))
    exit(1)

if __name__ == '__main__':
    main()
