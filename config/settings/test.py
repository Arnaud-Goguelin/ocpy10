from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

SECRET_KEY = "test-secret-key-not-for-production"

# DB in RAM to make tests faster, and reset after each test
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
