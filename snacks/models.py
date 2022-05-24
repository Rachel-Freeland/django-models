from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


class SnackDetailView(Snack):
    name = models.CharField(max_length=64)
    description = models.TextField()
    purchaser = models.ForeignKey(get_user_model(), models.CASCADE)
    pass