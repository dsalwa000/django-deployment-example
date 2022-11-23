from django.urls import path
from . import views

urlpatterns = [
    path('there/', views.view, name='first_view'),
]