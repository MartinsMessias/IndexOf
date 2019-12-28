from django.db import models

# Create your models here.
class Dork(models.Model):
    QUERY = (('Yes', 'Yes'),('Not', 'Not'))
    tag = models.CharField(max_length=250,default='')
    explanation = models.TextField(default='')
    dork = models.CharField(max_length=250, default='')
    query = models.CharField(choices=QUERY, max_length=3, default='Yes')

    def __str__(self):
        return self.tag