#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import logging
from urllib.parse import urljoin

dependencies_missing = False
try:
    import requests
except ImportError:
    dependencies_missing = True

from metasploit import module

metadata = {
    'name': 'Name of POC',
    'description': '''
        Python communication with msfconsole.
    ''',
    'authors': [
        'Jacob Robles'
    ],
    'date': '2022-3-31',
    'license': 'MSF_LICENSE',
    'references': [
        {'type': 'url', 'ref': 'https://blog.rapid7.com/2017/12/28/regifting-python-in-metasploit/'},
        {'type': 'aka', 'ref': 'Coldstone'}
    ],
    'type': 'single_scanner',
    'options': {
        'targeturi': {'type': 'string', 'description': 'The base path', 'required': True, 'default': '/'}
    }
}

def run(args):
    module.log('startxxxxxxxxxx')
    url = args['targeturi']
    headers = {
        "Content-Type":"application/x-www-form-urlencoded"
    }
    data = "test"
    try:

        go = requests.post(url,headers=headers, data=data, timeout=15, allow_redirects=False, verify=False)
        shellurl = urljoin(url, 'test.jsp')
        shellgo = requests.get(shellurl, timeout=15, allow_redirects=False, verify=False)
        if shellgo.status_code == 200:
            module.log(f"The vulnerability exists, the shell address is :{shellurl}?pwd=j&cmd=whoami", 'warning')
    except Exception as e:
        logging.error(e)
        module.log('{}'.format(e), 'warning')
        pass
    pass


if __name__ == '__main__':
    module.run(metadata, run)

