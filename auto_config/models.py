from django.db import models


class Provision(models.Model):
    site = models.CharField(max_length=5)
    output = models.TextField()
