from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):  #creating a class
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True )
    #participaints =
    update= models.DateTimeField(auto_now=True)
    create= models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-update', '-create']


    def __str__(self): #creating a function
        return self.name  
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)   #when the room is deleted all the msg related are deleted as well
    body = models.TextField()
    update= models.DateTimeField(auto_now=True)
    create= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[0:50]
        