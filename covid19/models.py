from django.db import models

# Create your models here.

"""
Student name: Van Phuc Tan Le
Student number: 040985238

This class specifies the model of each Record of the dataset
Each record is an object called CovidRecord
This class helps to map data to the database
and helps to handle each C-R-U-D operation.

-> Return None
"""


class CovidRecord(models.Model):
    uid = models.CharField(max_length=3)
    nameEN = models.CharField(max_length=100)
    nameFR = models.CharField(max_length=100)
    date = models.DateField()
    num_confirmed = models.CharField(max_length=10)
    num_probable = models.CharField(max_length=10)
    num_death = models.CharField(max_length=10)
    num_total = models.CharField(max_length=10)
    num_tested = models.CharField(max_length=10)
    rate_tested = models.CharField(max_length=10)
    num_today = models.CharField(max_length=10)
    rate_total = models.CharField(max_length=10)
