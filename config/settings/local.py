from .base import *


DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

# SQLite DB for dev
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Console email backend to test email in local
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
