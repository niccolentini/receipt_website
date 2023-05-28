from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('about/', views.aboutPage, name='aboutPage'),
    path('signup/', views.signupPage, name='signupPage'),
]