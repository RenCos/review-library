from django.urls import path
from . import views

urlpatterns = [
    #default path for russian welcome page
    path('', views.russianWelcomePage, name='russianWelcomePage' )
]
