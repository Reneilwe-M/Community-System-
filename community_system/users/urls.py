from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
   path('', views.login_view, name='home'), 
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
   # path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'), # catches Django's default redirect
path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
]