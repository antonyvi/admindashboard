from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.LoginPage, name='login'),
    path('signup/', views.SignupPage, name='signup'),
    
]