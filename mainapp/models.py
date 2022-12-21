from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User_Data(models.Model):
    tuser= models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=12,default="None")
    def __str__(self):
        return self.tuser


class Match_Data(models.Model):
    match_name=models.CharField(max_length=30,default="None")
    match_type = models.CharField(max_length=10)
    map = models.CharField(max_length=10)
    slots = models.IntegerField()
    timing = models.CharField(max_length=10)
    pricing = models.CharField(max_length=10,default="None")
    winning = models.CharField(max_length=70,default=0)
    def __str__(self):
        return self.match_name

class Register_Match(models.Model):
    gameid=models.CharField(max_length=30,default="xxx")
    pwd=models.CharField(max_length=30,default="xxx")
    username=models.CharField(max_length=40)
    flag_set=models.CharField(max_length=10,default="no")
    match_name=models.CharField(max_length=30)
    def __str__(self):
        return self.username

class Id_Pass(models.Model):
    gameid=models.CharField(max_length=30)
    pwd=models.CharField(max_length=30)
    match_name=models.CharField(max_length=30)
    def __str__(self):
        return self.match_name

    def save(self, *args, **kwargs):
        changeregmatch=Register_Match.objects.filter(match_name=self.match_name).update(flag_set="yes",gameid=self.gameid,pwd=self.pwd)
        super().save(*args, **kwargs)

class users_match(models.Model):
    player_name=models.CharField(max_length=30,default="Hello")
    mobile_number = models.CharField(max_length=12)
    payment = models.CharField(max_length=30,default="no")

    def __str__(self):
        return self.player_name

    def save(self, *args, **kwargs):
        changeregmatch=users_match.objects.filter(mobile_number=self.mobile_number).update(payment="yes")
        super().save(*args, **kwargs)
