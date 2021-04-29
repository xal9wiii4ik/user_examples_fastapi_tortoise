from core import py_env

SECRET_KEY = py_env.SECRET_KEY

# database settings
DATABASE_URL = (
    f"postgres://{py_env.POSTGRES_USER}:"
    f"{py_env.POSTGRES_PASSWORD}@"
    f"{py_env.POSTGRES_SERVER}:"
    f"{py_env.POSTGRES_PORT}/"
    f"{py_env.POSTGRES_DB}"
)
APPS_MODELS = [
    "apps.auth.models",
    "apps.social_account.models",
    "apps.user.models",
    "aerich.models",
]

# settings for jwt authentication
TOKEN_TYPE = py_env.TOKEN_TYPE
ALGORITHM = py_env.ALGORITHM
ACCESS_TOKEN_JWT_SUBJECT = py_env.ACCESS_TOKEN_JWT_SUBJECT
# Token 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8

# settings for smtp
EMAIL_HOST = py_env.EMAIL_HOST
EMAIL_HOST_PASSWORD = py_env.EMAIL_HOST_PASSWORD
EMAIL_HOST_USER = py_env.EMAIL_HOST_USER
EMAIL_PORT = py_env.EMAIL_PORT
EMAIL_USE_TLS = py_env.EMAIL_USE_TLS
EMAIL_USERNAME = py_env.EMAIL_USERNAME

# superuser settings
USERNAME_SUPERUSER = py_env.USERNAME_SUPERUSER
EMAIL_SUPERUSER = py_env.EMAIL_SUPERUSER
PASSWORD_SUPERUSER = py_env.PASSWORD_SUPERUSER
REPEAT_PASSWORD_SUPERUSER = py_env.REPEAT_PASSWORD_SUPERUSER

# git hub
CLIENT_ID = py_env.CLIENT_ID
CLIENT_SECRET = py_env.CLIENT_SECRET
