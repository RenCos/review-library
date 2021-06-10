from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path for russian app
    path('rus', include('site_rus.urls')),
    #path for english app
    path('', include('site_eng.urls'))
]
