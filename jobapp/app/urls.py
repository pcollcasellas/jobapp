from django.urls import path

from app import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:id>', views.job_detail, name='job_detail')
]
