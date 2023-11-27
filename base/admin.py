from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message 

admin.site.register(Room) #to work with room on admin panel
admin.site.register(Topic)
admin.site.register(Message)