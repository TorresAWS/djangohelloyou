import os
import sys
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
#SECRET_KEY = os.environ.get ('SECRET_KEY', {{ secret_key }} )
SECRET_KEY = os.environ.get ('SECRET_KEY', os.urandom(32))
ALLOWED_HOSTS = os.environ.get ('ALLOWED_HOSTS', 'localhost'.split(','))
BASE_DIR = os.path.dirname(__file__)
####


settings.configure(
 DEBUG=DEBUG,
 SECRET_KEY=SECRET_KEY,
 ALLOWED_HOSTS=ALLOWED_HOSTS,
 SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'), 
 SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR, '_build'), 
 STATIC_ROOT=os.path.join(BASE_DIR, '_build', 'static'), 
 ROOT_URLCONF='sitebuilder.urls',
 MIDDLEWARE_CLASSES = (),
 INSTALLED_APPS=(
     'django.contrib.staticfiles',
     'sitebuilder',
), 
 TEMPLATES=(
   {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True, 
   },
 ),
  STATIC_URL='/static/',

)



if __name__ == "__main__":
  from django.core.management import execute_from_command_line
  execute_from_command_line(sys.argv)
