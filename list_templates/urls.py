from django.urls import path
from list_templates import views

urlpatterns = [
    path('',views.index),
    path('template',views.template),
    path('dashboard',views.dashboard)
]
