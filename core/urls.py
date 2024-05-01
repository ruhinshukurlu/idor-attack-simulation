from django.urls import path
from core.views import *


urlpatterns = [
    path('', home, name='index'),
    path('login', user_login, name='login'),
    path('register', register, name='register'),
    path('logout', user_logout, name='logout'),
    path('profile/<int:id>', user_profile, name='profile'),
    path('payment', payment, name='payment'),
]
