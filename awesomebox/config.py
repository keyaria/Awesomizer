"""
Awesomebox development configuration.

"""

import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xa2$d\x90\xf0\x97O\xe29O,\xea\x80\xf9\xb2\x13,\xd8\x82v\xfd\x86r\x00'  # noqa: E501  pylint: disable=line-too-long
SESSION_COOKIE_NAME = 'login'

# Database file is var/database.db
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'database.db'
)
