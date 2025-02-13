import os
from pathlib import Path

# Construcción de rutas dentro del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NicolasTp$Supermercado',
        'USER': 'NicolasTp',
        'PASSWORD': 'Eureka00+',
        'HOST': 'NicolasTp.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

# Clave de seguridad
SECRET_KEY = 'django-insecure-your-secret-key-here'

# Modo de depuración
DEBUG = True

# Hosts permitidos
ALLOWED_HOSTS = ['NicolasTp.pythonanywhere.com']

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',  # Middleware para servir archivos estáticos de manera eficiente
    'productos',
]

# Configuración de middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise para archivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de archivos estáticos
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'productos/static'),  # Accede directamente a la subcarpeta correcta
]


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# Excluir archivos innecesarios como admin, vendor, etc.
WHITENOISE_KEEP_ONLY_STATICFILES = True

# Configuración de almacenamiento de archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Evita errores si falta algún archivo en el manifest
WHITENOISE_MANIFEST_STRICT = False

# Configuración de archivos de medios
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración de internacionalización
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True
