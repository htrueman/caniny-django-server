from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ""
EMAIL_HOST_USER = 'no-reply@caniny.com'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
HOST_NAME = 'http://127.0.0.1:8001'
