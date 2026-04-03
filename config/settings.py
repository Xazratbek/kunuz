from pathlib import Path
import ssl

BASE_DIR = Path(__file__).resolve().parent.parent

import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()

SECRET_KEY = 'django-insecure-%owe3pvpkti=ms&rd2zhuqme)dgid3-rn4$(jsas967y%@a_1k'

DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "https://7d05-213-230-91-82.ngrok-free.app"
]

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "https://7d05-213-230-91-82.ngrok-free.app",
    "https://*.ngrok-free.app",
    "https://*.ngrok.io",
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    "corsheaders",
    'news',
    'accounts',
    'django_ckeditor_5',

]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath("templates"))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'news.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'uz'

LANGUAGES = [
    ('uz', 'O\'zbekcha'),
    ('ru', 'Ruscha'),
    ('en', 'Inglizcha'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

CKEDITOR_5_UPLOAD_FILE_VIEW_NAME = "/static/ckeditor/ckeditor/"

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|', 'bulletedList', 'numberedList',
            '|', 'blockQuote',
        ],
        'toolbar': ['undo', 'redo', '|', 'heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link',
                    'underline', 'strikethrough', 'code', 'subscript', 'superscript', 'highlight', '|',
                    'codeBlock', 'sourceEditing', 'insertImage', 'insertTable', '|',
                    'bulletedList', 'numberedList', 'todoList', '|', 'blockQuote', 'imageUpload', 'mediaEmbed', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'removeFormat',
                    'alignment', 'horizontalLine', 'pageBreak'],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignCenter', 'imageStyle:alignRight', 'imageStyle:fullWidth', '|',
                        'linkImage', 'imageInsert'],
            'styles': [
                'full',
                'side'
            ]
        },
        'mediaEmbed': {
            'previewsInData': True,
            'providers': [
                'youtube', 'vimeo', 'instagram', 'twitter', 'googleMaps', 'flickr', 'dailymotion', 'spotify', 'codepen', 'soundcloud'
            ]
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells',
                               'tableProperties', 'tableCellProperties'],
            'tableToolbar': ['bold', 'italic']
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'xazratbek123@gmail.com'
EMAIL_HOST_PASSWORD = 'qvqn blcp wrnq orkt'
DEFAULT_FROM_EMAIL = 'xazratbek123@gmail.com'

EMAIL_SSL_CONTEXT = ssl._create_unverified_context()

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"

LOGIN_REDIRECT_URL = "article-list"
LOGOUT_REDIRECT_URL = "article-list"

# Password Reset
PASSWORD_RESET_TIMEOUT = 3600  # 1 hour in seconds

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"