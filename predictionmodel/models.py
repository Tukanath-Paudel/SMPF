from django.db import models

# Create your models here.
class Inputform(models.Model):
    company_name = models.CharField(max_length=100)
