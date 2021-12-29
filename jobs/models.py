from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    image = models.ImageField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=100)
    proficiency = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
