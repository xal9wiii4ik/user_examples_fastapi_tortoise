from tortoise import models, fields, Tortoise


class User(models.Model):
    """ Model user """

    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=50, unique=True)
    hashed_password = fields.CharField(max_length=100)
    is_active = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}: {self.username} {self.email} is_active: {self.is_active} is_superuser: {self.is_superuser}'


# Tortoise.init_models(["apps.user.models"], "models")
