from django.urls import path

from . import views
urlpatterns = [
path('signin', views.sign_in, name='login'),
path('register', views.register, name='register'),

]