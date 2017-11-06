from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='i$+#4@f+2t8)5h=(tmb4_6kc1+p9fhq2+ifg4yq*a995najojt')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
