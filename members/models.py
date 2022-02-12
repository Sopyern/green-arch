from django.db import models

# Create your models here.

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=100)
    note = models.TextField()
    position = models.CharField(max_length=100)
    picture = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.body[:20] + "..."
