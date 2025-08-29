from django.db import models

# Create your models here.
class Parent(models.Model):
	
	Parentname=models.CharField(max_length=20)
	number=models.IntegerField()
	Email=models.EmailField()
	Studentname=models.CharField(max_length=20)
	Message=models.CharField(max_length=20)

class Contact(models.Model):
	
	name=models.CharField(max_length=20)
	number=models.IntegerField()
	Email=models.EmailField()
	Message=models.CharField(max_length=20)
