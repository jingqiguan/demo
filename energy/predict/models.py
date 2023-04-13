from django.db import models
from django.contrib.auth.models import User


class Node(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Price(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    rtm = models.FloatField()


class Transaction(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_created=True)
    rtm = models.FloatField()
    units = models.FloatField()
    action = models.CharField(max_length=10, default="Buy")


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    kwh = models.FloatField(default=0)
