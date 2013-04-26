
DEBUG = True 

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = "*.asf.alaska.edu"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'DAACDEV',                      # Or path to database file if using sqlite3.
        'USER': 'asfadm',                      # Not used with sqlite3.
        'PASSWORD': 'Asf4d|\/|',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
