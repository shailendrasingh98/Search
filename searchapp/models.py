from django.db import models

# Create your models here.
# This not used yet as we are not usinig database
class Words_Search(models.Model):
    words = models.CharField(max_length = 100)
    frequency  = models.IntegerField()

    def __str__(self):
        return self.words
