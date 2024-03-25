from django.urls import path
from core.views import home, user_login, register, user_logout, user_profile


urlpatterns = [
    path('', home, name='index'),
    path('login', user_login, name='login'),
    path('register', register, name='register'),
    path('logout', user_logout, name='logout'),
    path('profile/<int:id>', user_profile, name='profile'),
]
