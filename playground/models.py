from django.db import models

# Create your models here.
class Users(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)

class Todo(models.Model):
    sno=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=122)
    desc=models.CharField(max_length=500)
    date_created=models.DateField()


