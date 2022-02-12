from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    location = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    design_by = models.TextField()
    drawn_by = models.TextField()
    thumbnail = models.ImageField(default="default.png", blank=True)
    persfective1 = models.ImageField(default="default.png", blank=True)
    persfective2 = models.ImageField(default="default.png", blank=True)
    persfective3 = models.ImageField(default="default.png", blank=True)
    persfective4 = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:20] + "..."
