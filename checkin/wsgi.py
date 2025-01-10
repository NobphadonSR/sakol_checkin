import os
import sys

path = '/home/cloverzen27ns/checkin'
if path not in sys.path:
    sys.path.append(path)

print("Current sys.path:")
print(sys.path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'checkin.settings'

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception as e:
    print(f"Error loading application: {e}")