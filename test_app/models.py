from django.db import models


# Create your models here.


class TestModel(models.Model):
    name = models.CharField(max_length=50)


class TestModel2(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
