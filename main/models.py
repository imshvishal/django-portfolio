from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class ContactFormData(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=256)
    message = models.CharField(max_length=1500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id}. {self.name}"

class Config(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    url = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
        
class Skill(models.Model):
    name = models.CharField(max_length=32)
    percentage = models.IntegerField()    
    def __str__(self):
        return f"{self.name} ({self.percentage})"

class SocialMedia(models.Model):
    name = models.CharField(max_length=32)
    link = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name

class WebData(models.Model):
    id = models.CharField(max_length=32, primary_key=True)    
    name = models.CharField(max_length=32)
    short_descr = models.CharField(max_length=100)
    med_descr = models.CharField(max_length=200)
    long_descr = models.CharField(max_length=1000)
    socialmedias = models.ManyToManyField(SocialMedia, blank=True)
    email = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    status = models.CharField(max_length=32)
    skills = models.ManyToManyField(Skill, blank=True)
    
    def __str__(self) -> str:
        return self.name