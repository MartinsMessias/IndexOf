from django.db import models

# Create your models here.
class Dork(models.Model):
    tag = models.CharField(max_length=250)
    explanation = models.TextField()
    dork = models.CharField(max_length=250)

    def __str__(self):
        return self.tag