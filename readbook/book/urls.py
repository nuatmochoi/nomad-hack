from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='book'
urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(), name= 'login'),
    path('login/', views.LoginView.as_view(), name='login')
]