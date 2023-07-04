from django.db import models

# Create your models here.
class Member(models.Model):
  fullname = models.CharField(max_length=255)
  mobile_number = models.CharField(max_length=255)