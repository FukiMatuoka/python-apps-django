from django.test import TestCase

# Create your tests here.

STATIC_URL = "/static/"  # これはデフォルトであるはず
STATICFILES_DIRS = [BASE_DIR / "work05" / "static"]  # ← これを追加！
