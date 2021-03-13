# IntroduccionADjango
Repositorio para la conferencia Introducción a Django 13 de marzo de 2021

## Para iniciar
- Crear entorno virtual con "pipenv shell"
- Instalar Django con "pipenv install django"
- Iniciar proyecto con "django-admin startproject NOMBRE ."
- Iniciar aplicaciones con "python manage.py startapp NOMBRE"
## Configurar archivos staticos
- STATIC_URL = '/static/
- STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
- STATICFILES_FINDERS = [
  "django.contrib.staticfiles.finders.FileSystemFinder",
  "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
## Configurar plantillas 
- Dentro de TEMPLATES -> 'DIRS': [os.path.join(BASE_DIR, 'templates')],
