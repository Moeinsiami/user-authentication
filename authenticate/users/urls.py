from django.urls import path
from .views import register_user, login_user, logout_user, home

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('home/', home, name='home'), 
]
