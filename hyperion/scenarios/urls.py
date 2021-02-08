from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<scenario_id>/raw_messages/', views.raw_messages, name='raw_messages')
]