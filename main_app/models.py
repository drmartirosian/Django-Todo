from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name