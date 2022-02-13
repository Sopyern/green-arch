from django.apps import AppConfig


class MembersConfig(AppConfig):
    name = 'members'

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'blog'
