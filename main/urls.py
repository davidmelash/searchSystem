from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name='login'),
    path('profile/', views.get_profile, name='profile'),
]