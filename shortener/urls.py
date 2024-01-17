from django.urls import path
from . import views
from .views import shorten_url, delete_url


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('shorten/', views.shorten_url, name='shorten_url'),
    path('delete/<str:short_url>/', views.delete_url, name='delete_url'),
    path('s/<str:short_url>/', views.find_long_url, name='find_long_url'),

]

