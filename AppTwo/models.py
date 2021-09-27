
from django.db import models


# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UserNames(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)


class NewUserReg(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    v_email = models.EmailField()
    text = models.CharField(max_length=500)
