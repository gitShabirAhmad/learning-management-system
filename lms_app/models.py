from django.db import models

# Create your models here.
class Cls(models.Model):
    name = models.CharField(max_length=45)
    time = models.CharField(max_length=45)
    started_date = models.DateField()

    def __str__(self):
        return self.name

