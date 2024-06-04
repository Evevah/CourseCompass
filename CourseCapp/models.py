from django.db import models
from datetime import datetime
# Create your models here.
class Feature(models.Model):
    
    name  = models.CharField(max_length=2000)

    details = models.CharField(max_length=2000)


class Section1(models.Model): 
    quest = models.CharField(max_length=2000, default='Question')
    answer = models.CharField(max_length = 2000, default='answer')

class Section2(models.Model): 
    quest = models.CharField(max_length=2000, default='Question')
    answer = models.CharField(max_length = 2000, default='answer')

class Section3(models.Model): 
    quest = models.CharField(max_length=2000, default='Question')
    answer = models.CharField(max_length = 2000, default='answer')

class Section4(models.Model): 
    quest = models.CharField(max_length=2000, default='Question')
    answer = models.CharField(max_length = 2000, default='answer')


class results(models.Model):
    career = models.CharField(max_length=100, default='career')
    description = models.CharField(max_length=5000, default='description')
    best_course = models.CharField(max_length=100, default='best')
    prospects = models.CharField(max_length=100, default='prospects')

class Room(models.Model):
    name = models.CharField(max_length=2000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class COMUD(models.Model):
    email = models.CharField(max_length=100)
    Option1C = models.CharField(max_length=1000)
    Option1D = models.CharField(max_length=1000)
    Option1B = models.CharField(max_length=1000)
    Option1P = models.CharField(max_length=1000)

    Option2C = models.CharField(max_length=1000)
    Option2D = models.CharField(max_length=1000)
    Option2B = models.CharField(max_length=1000)
    Option2P = models.CharField(max_length=1000)

    Option3C = models.CharField(max_length=1000)
    Option3D = models.CharField(max_length=1000)
    Option3B = models.CharField(max_length=1000)
    Option3P = models.CharField(max_length=1000)

