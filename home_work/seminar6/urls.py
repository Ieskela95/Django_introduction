from django.urls import path, include
from seminar6 import views

urlpatterns = [
    path('', views.seminar6, name='seminar6'),
    path('db/', views.total_in_db, name='total_in_db'),
    path('view/', views.total_in_view, name='total_in_view'),
    path('template/', views.total_in_template, name='total_in_template'),
]
