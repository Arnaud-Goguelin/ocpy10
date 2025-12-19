import os
import sys

from ..constants import Environment

environment = os.environ.get('ENVIRONMENT', Environment.local.value)
# use print and not logging in this file as it is executed before logging is configured
if environment == Environment.production.value:
    print("⚠️  Production environment is not configured yet. Application is only available in local environment.", file=sys.stderr)
    sys.exit(1)
    # from .prod import *
elif environment == Environment.test.value:
    print("⚠️  Test environment is not configured yet. Application is only available in local environment.",
          file=sys.stderr)
    sys.exit(1)
    # from .test import *
else:
    from .local import *
    print()
    print(f"🚀 Django run in: {environment} environment.")
    print("📖 Docs access to : "
          "\nhttp://127.0.0.1:8000/api/docs/swagger/, "
          "\nhttp://127.0.0.1:8000/api/docs/redoc/")
    print()
