from .base import *

DEBUG = True

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'Nexu'
EMAIL_HOST_PASSWORD = 'vege12ve'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
HOST_NAME = 'http://165.22.152.38'

REDIRECT_URL = 'http://165.22.152.38/registration'
