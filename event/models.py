from django.db import models
import datetime

class Study(models.Model):
    subject = models.CharField(max_length=200)
    time = models.TimeField(null=True, default="00:00")
    memo = models.CharField(max_length=500, default="記録なし")

    textbook_name = models.CharField(max_length=200, null=True, default="記録なし")
    peji1 = models.IntegerField(null=True, default=0)
    peji2 = models.IntegerField(null=True, default=0)
    created = models.DateTimeField(auto_now_add=True)


class kyouka(models.Model):
    kyouka = models.CharField(max_length=100)

    
class diary(models.Model):
    tenki1 = models.CharField(max_length=50, default="記録なし")
    tenki2 = models.CharField(max_length=50, default="記録なし")
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=300, default="記録なし")
    text = models.CharField(max_length=1000, default="記録なし")
    hitokoto = models.CharField(max_length=100, default="記録なし")
    sonohoka = models.CharField(max_length=300, default="記録なし")


class dd(models.Model):
    date = models.DateField(default=datetime.date.today)
    jinbutu = models.CharField(max_length=400, default="記録なし")
    title = models.CharField(max_length=300, default="記録なし")
    text = models.CharField(max_length=1000, default="記録なし")
    kansou = models.CharField(max_length=1000, default="記録なし")


class smoke(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, default="記録なし")
    mg = models.IntegerField(default=0)
    honn = models.IntegerField(default=0)
    memo = models.CharField(max_length=500, default="記録なし")


class diet(models.Model):
    date = models.DateField(default=datetime.date.today)
    height = models.IntegerField(default=0)
    kg = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    bmi = models.CharField(max_length=100, default="計算できませんでした")

    play = models.CharField(max_length=100, null=True, default="記録なし")
    time = models.TimeField(null=True, default="00:00")



class eat(models.Model):
    date = models.DateField(default=datetime.date.today)
    morning = models.CharField(max_length=1000, default="記録なし")
    lunch = models.CharField(max_length=1000, default="記録なし")
    dinner = models.CharField(max_length=1000, default="記録なし")
    sonohoka = models.CharField(max_length=1000, default="記録なし")
    eat_time = models.TimeField(null=True, default="記録なし")