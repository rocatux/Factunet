from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import login_page, logout_page

urlpatterns = [
    path('accounts/login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]