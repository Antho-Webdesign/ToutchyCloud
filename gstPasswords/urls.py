from django.urls import path

from gstPasswords.views import home_passwords, listall

urlpatterns = [
    path('', home_passwords, name='home_passwords'),
    path('listall/', listall, name="listall"),
]