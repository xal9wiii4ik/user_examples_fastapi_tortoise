from tortoise import models, fields, Tortoise


class Uid(models.Model):
    """Model uid for future verification of user"""

    uid = fields.CharField(max_length=100)
    user = fields.ForeignKeyField(
        model_name='models.User', related_name='uid_user', null=True, on_delete=fields.CASCADE
    )
    social_user = fields.ForeignKeyField(
        model_name='models.SocialAccount', related_name='uid_social_account', null=True, on_delete=fields.CASCADE
    )

    def __str__(self):
        return f'{self.pk}: {self.user} or {self.social_user}'
