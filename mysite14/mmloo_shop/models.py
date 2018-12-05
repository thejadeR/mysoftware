from django.db import models

# Create your models here.
class UserInfo(models.Model):

    db_uname = models.CharField(max_length=100)
    db_upassword = models.CharField(max_length=100)
