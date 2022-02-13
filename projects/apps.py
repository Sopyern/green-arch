from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = 'projects'
    
    
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'blog'
