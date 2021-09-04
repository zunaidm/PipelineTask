from django.db import models

# Create your models here.

class Log(models.Model):
    date_time = models.CharField(max_length=50)
    category = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.date_time, self.category, self.message