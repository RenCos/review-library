from django.urls import path
from . import views

urlpatterns = [
    #default path for welcome page
    path('',views.welcomePage, name='welcomePage' )
]