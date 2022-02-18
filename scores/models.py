from django.db import models

# Create your models here.


class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)
