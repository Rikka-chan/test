from django.db import models


class Candidate(models.Model):
    photo_url = models.URLField(default=None)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    birthday = models.DateField()
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField()
    salary = models.IntegerField()
