from django.contrib import admin
from django.urls import path
from apptsc import views

urlpatterns = [
    path('timestamp_to_time/<str:timestamp>/<str:area>/<str:city>/', views.timestamp_to_time, name='TimeStamp to Time'),
    path('time_to_timestamp/<str:datetime>/<str:area>/<str:city>/', views.time_to_timestamp, name='Time to TimeStamp')
]
