from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('services', services, name="services"),
    path('contact_form', contact_form, name="contact_form"),
    path('register', register_form, name="register"),
]