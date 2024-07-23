import os
import sys
import django

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def pytest_configure():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'parserator_web.settings'
    django.setup()
