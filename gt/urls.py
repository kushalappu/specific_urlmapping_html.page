app_name='anything'
from django.urls import path
from gt.views import *

urlpatterns = [
    path('hardik/',hardik,name='hardik'),
]