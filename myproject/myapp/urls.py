from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Optional home page
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]