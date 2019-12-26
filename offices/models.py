from django.db import models


# Create your models here.
class ExecutiveOffice(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class LegislativeOffice(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class JudiciaryOffice(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


# for provincial government
class ProvinceJudiciaryOffice(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
