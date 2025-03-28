from django.contrib import admin
from django.urls import include, path
from . import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views

app_name = 'django_models'
urlpatterns = [
    path('', views.save_example, name='upload_example'),
    # path('thanks/', views.upload_file),
    path('thanks/', views.thanks),
    path('pub/', views.PublisherListView.as_view()),
    # path('pub/<publisher>/', views.PublisherDetailView.as_view()),

    # class views
    path('pub/add/', views.PublisherCreateView.as_view(), name='pub-add'),
    path('pub/<int:pk>/', views.PublisherUpdateView.as_view(), name='pub-update'),
    path('pub/<int:pk>/delete/', views.PublisherDeleteView.as_view(), name='pub-del'),

    # accounts
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/profile/', auth_views.LoginView.as_view(template_name='django_models/index.html')),
    path('accounts/login/', views.MyLogin.as_view()),
    path('accounts/profile/', views.MyProfile.as_view()),
]