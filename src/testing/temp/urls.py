from django.urls import path
from . import views

app_name = 'temp'

urlpatterns = [
    path('main', views.inh_temp_main, name='main'),
    path('new', views.inh_temp_new_page, name='new'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('special', views.special, name='special'),

]