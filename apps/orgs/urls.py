from django.urls import path, re_path
from orgs import views

app_name = 'orgs'
urlpatterns = [
    re_path('org_list/$', views.org_list, name='org_list'),
    re_path('org_detail/(\d+)/$', views.org_detail, name='org_detail'),
]
