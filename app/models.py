from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)

class RegisterForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    college = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=10)
    course_year = models.CharField(max_length=4)
    course_selected = models.CharField(max_length=200)