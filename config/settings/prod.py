from .base import *

DEBUG = True

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'  # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = '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'  # this is your API key
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'no-reply@caniny.com'  # this is the sendgrid email

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
HOST_NAME = 'http://165.22.152.38'

REDIRECT_URL = 'http://165.22.152.38/registration'
