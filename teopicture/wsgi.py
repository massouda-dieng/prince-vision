import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teopicture.settings')

application = get_wsgi_application()

# Migrations automatiques au démarrage
try:
    from django.core.management import call_command
    call_command('migrate', '--run-syncdb', verbosity=0)
except Exception as e:
    print(f"Migration warning: {e}")