from django.db import models

# Create your models here.


class Albums(models.Model):
    name=models.CharField(max_length=100)
    stars=models.IntegerField()

    def __str__(self):
        return self.name
