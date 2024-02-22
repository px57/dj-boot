"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'load_basic_data/', 
        views.load_basic_data, 
        name='boot_load_basic_data'
    ),
]