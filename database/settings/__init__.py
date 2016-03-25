import os

ENVIRONMENT = os.getenv("DJANGO_ENVIRONMENT")

if not ENVIRONMENT:
    ENVIRONMENT = 'production'

if ENVIRONMENT == 'production':
    from production import *
elif ENVIRONMENT == 'dev':
    from dev import *