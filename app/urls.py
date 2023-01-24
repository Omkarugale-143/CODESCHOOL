from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('contact_form', contact_form, name="contact_form"),
]