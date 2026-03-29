from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_issue, name='home'),
    path('track/', views.track_issues, name='track'),
    path('report/', views.report_issue, name='report'),
   path('staff/', views.staff_dashboard, name='staff_dashboard'),
   path('register/', views.register, name='register'),
   path('staff/update/<int:issue_id>/', views.update_issue, name='update_issue'),



]