from core.config import DATABASE_URL, APPS_MODELS

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": APPS_MODELS,
            "default_connection": "default",
        }
    },
}
