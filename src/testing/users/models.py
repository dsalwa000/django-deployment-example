from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)

    def __str__(self):
        return self.name


















