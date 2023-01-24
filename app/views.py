from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

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
