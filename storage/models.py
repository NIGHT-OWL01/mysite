from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ContactRelation(models.Model):
    relation_type = models.CharField(max_length=100)

    def __str__(self):
        return self.relation_type

class Contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number = models.PositiveIntegerField()
    relation = models.ForeignKey('ContactRelation',on_delete=models.CASCADE)
