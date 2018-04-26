import dj_database_url

from Epsy.settings import *


DEBUG = os.environ.get('DEBUG', False)
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

SECRET_KEY = get_env_variable("SECRET_KEY")

# Databases and Storage

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)