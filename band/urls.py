from django.urls import path
from . import views


app_name = 'band'

urlpatterns = [
    path('', views.home, name='home'),
    path('music/', views.music, name='music'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

]
