from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'band'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('music/', views.music, name='music'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('static/band/images/', views.music, name='music'),
]
