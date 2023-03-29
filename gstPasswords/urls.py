from django.urls import path

from gstPasswords.views import home_passwords

urlpatterns = [
    path('', home_passwords, name='home_passwords'),
]