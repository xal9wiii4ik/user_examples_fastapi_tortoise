from tortoise import models, fields, Tortoise


class SocialAccount(models.Model):
    """ Model for social account """

    account_id = fields.IntField()
    username = fields.CharField(max_length=50)
    email = fields.CharField(max_length=50, null=True)
    provider = fields.CharField(max_length=50)
    user = fields.ForeignKeyField(
        model_name='models.User', related_name='social_user', null=True, on_delete=fields.CASCADE,
    )

    def __str__(self):
        return f'{self.pk}: {self.username} {self.provider} {self.email} {self.user}'


# Tortoise.init_models(["apps.social_account.models"], "models")
