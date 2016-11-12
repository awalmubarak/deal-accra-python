from django.db import models


class Deal(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=5000)
    image = models.FileField()
    Contact_number = models.CharField(max_length=100);

    def __str__(self):
        return self.title
