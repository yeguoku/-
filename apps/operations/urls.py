from django.urls import path, re_path
from operations import views

app_name = 'operations'
urlpatterns = [
    re_path('user_ask/$', views.user_ask, name='user_ask'),
]
