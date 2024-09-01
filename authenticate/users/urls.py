from django.urls import path
from .views import register_user, login_user, logout_user, dashboard, home, update_email

urlpatterns = [
    path('', home, name='home'), 
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('dashboard/', dashboard, name='dashboard'),
    path('update-email/', update_email, name='update_email'),
]
