
from django.contrib import admin
from django.urls import path
from postgresapp.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',student.as_view()),
]

urlpatterns += staticfiles_urlpatterns() 