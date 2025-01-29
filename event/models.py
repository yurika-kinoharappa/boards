from django.db import models
import datetime

class Study(models.Model):
    subject = models.CharField(max_length=200)
    time = models.TimeField(null=True)
    memo = models.CharField(max_length=500)

    textbook_name = models.CharField(max_length=200, null=True)
    peji1 = models.IntegerField(null=True, default=0)
    peji2 = models.IntegerField(null=True, default=0)
    created = models.DateTimeField(auto_now_add=True)

class diary(models.Model):
    tenki1 = models.CharField(max_length=50, default="記録なし")
    tenki2 = models.CharField(max_length=50, default="記録なし")
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=1000)
    hitokoto = models.CharField(max_length=100)
    sonohoka = models.CharField(max_length=300)


class dd(models.Model):
    date = models.DateField(default=datetime.date.today)
    jinbutu = models.CharField(max_length=400)
    title = models.CharField(max_length=300, default="なし")
    text = models.CharField(max_length=1000)
    kansou = models.CharField(max_length=1000)


class smoke(models.Model):
    date = models.DateField(default=datetime.date.today)
    name = models.CharField(max_length=200)
    mg = models.IntegerField(default=0)
    honn = models.IntegerField(default=0)
    memo = models.CharField(max_length=500)


class diet(models.Model):
    date = models.DateField(default=datetime.date.today)
    height = models.IntegerField(default=0)
    kg = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    bmi = models.CharField(max_length=100)

    play = models.CharField(max_length=100, null=True)
    time = models.TimeField(null=True)



class eat(models.Model):
    date = models.DateField(default=datetime.date.today)
    morning = models.CharField(max_length=1000, default="")
    lunch = models.CharField(max_length=1000, default="")
    dinner = models.CharField(max_length=1000, default="")
    sonohoka = models.CharField(max_length=1000, default="")
    eat_time = models.TimeField(null=True, default="なし")