DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'hello_django',
        'PASSWORD': 'AgJHn567H%',
        'HOST': 'localhost',
        'PORT': '',
    }
}