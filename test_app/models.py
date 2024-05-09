from django.db import models


# Create your models here.


class TestModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TestModel2(models.Model):
    name = models.CharField(max_length=100, verbose_name="something", blank=True, null=True)

    def __str__(self):
        return self.name
