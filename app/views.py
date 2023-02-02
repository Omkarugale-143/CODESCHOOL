from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def services(request):
    return render(request, 'app/services.html')

def contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contactForm = ContactForm(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        contactForm.save()
        messages.success(request, 'We\'ll reach out to you soon!!')
        return redirect('index')

def register_form(request):
    if request.method=="POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        college = request.POST.get("College")
        mobile_no = request.POST.get("Contact")
        course_year = request.POST.get("CourseYear")
        course = request.POST.get("Course")


        registerForm = RegisterForm(
            name = name,
            email = email,
            college = college,
            mobile_no = mobile_no,
            course_year = course_year,
            course_selected = course
        )
        registerForm.save()
        messages.success(request, 'Thank you for registering!!')
        return redirect('index')