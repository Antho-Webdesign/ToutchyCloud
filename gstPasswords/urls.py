from django.urls import path

from gstPasswords.views import home_passwords, listall, deleterecord, search

urlpatterns = [
    path('', home_passwords, name='home_passwords'),
    path('listall/', listall, name="listall"),
    path('recherche', search, name="search"),
    path('delete/<int:id>/', deleterecord, name="deleterecord"),
]