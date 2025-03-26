from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'django_models'
urlpatterns = [
    path('', views.save_example, name='upload_example'),
    # path('example/', views.upload_file)
]