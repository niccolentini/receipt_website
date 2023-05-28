from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('about/', views.aboutPage, name='aboutPage'),
    path('signup/', views.signupPage, name='signupPage'),
    path('login/', auth_views.LoginView.as_view(template_name='core/loginPage.html', authentication_form=LoginForm), name='loginPage'),
]