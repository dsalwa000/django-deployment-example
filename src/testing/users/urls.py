from django.urls import path
from .views import users_list, fill_form, fill_form_model

app_name = 'users'

urlpatterns = [
    path('', users_list, name='users_list'),
    path('form', fill_form, name='fill_form'),
    path('form2', fill_form_model, name='fill_form_model'),
]