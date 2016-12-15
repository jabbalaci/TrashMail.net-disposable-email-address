#!/usr/bin/env python

"""
Create a temporary (disposable) email address on trashmail.net .

I took the file https://trashmail.com/files/trashmail_sdk_1_1.tar.gz
and converted it to Python.

On https://trashmail.com/ you will have to register yourself (it's free).
Upon registration you provide your real email address where emails from
the disposable addresses will be redirected to. You need this registration
to be able to create disposable email addresses on trashmail.net .

Written by Laszlo Szathmary, 2013 (jabba.laci@gmail.com).
https://github.com/jabbalaci/TrashMail.net-disposable-email-address
"""

import re
import json
import requests

import utils
from clipboard import text_to_clipboards

USERNAME = None
PASSWORD = None
#
DEBUG = False


def get_session_id_and_real_email():
    """
    Login and get a session ID and your real email.
    """
    payload = {
        "api": 1,
        "cmd": "login",
        "fe-login-user": USERNAME,
        "fe-login-pass": PASSWORD
    }
    r = requests.post('https://trashmail.com/', data=payload)
    if DEBUG:
        print r.headers
    # Holy shit: you need the SECOND session ID, not the first one!
    session_id = re.findall(r"trashmail_session=(.*?);", r.headers['set-cookie'])[-1]
    if DEBUG:
        print session_id
    real_email = r.json()['msg']['real_email_list'].keys()[0]

    return session_id, real_email


def create_temp_email(session_id, real_email):
    """
    Create a new disposable email address.

    For this, we need to provide the session ID.
    The real email address must be given too where
    emails will be redirected to.
    """
    payload = {
        "data": {
            "id": -1,
            "uid": None,
            "ctime": 0,
            "ctime_text": "",
            "disposable_name": utils.get_urandom_password(8),
            "disposable_domain": "trashmail.com",
            "destination": real_email,
            "forwards": 10,     # that's the maximum number of forwards for the free service
            "expire": 7,        # max. value: 31 (one month)
            "website": "",
            "cs": 0,
            "notify": True,
            "desc": ""
        }
    }
    cookie = {'trashmail_session': session_id}
    headers = {'content-type': 'text/plain'}

    r = requests.post('https://trashmail.com/?api=1&cmd=update_dea',
        cookies=cookie, data=json.dumps(payload), headers=headers
    )
    if DEBUG:
        print r.text
    data = r.json()['data'][0]
    temp_email = "{0}@{1}".format(data['disposable_name'], data['disposable_domain'])

    return temp_email


def main():
    session_id, real_email = get_session_id_and_real_email()
    email = create_temp_email(session_id, real_email)

    # Uncomment to copy email to clipboard
    # Requires "xsel"

    # text_to_clipboards(email)
    # print '# copied to the clipboard'

    print email

#############################################################################

if __name__ == "__main__":
    if USERNAME and PASSWORD:
        main()
    else:
        print """Create a TrashMail.net disposable email address
You must provide the username and password that you use
on trashmail.net to access the address manager"""
        if not USERNAME:
            USERNAME = raw_input("Username: ")
        else:
            print "Username:", USERNAME
        if not PASSWORD:
            PASSWORD = raw_input("Password: ")
        else:
            print "Password:", '*' * len(PASSWORD)
        main()
