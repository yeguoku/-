from django.urls import path, re_path
from users import views
app_name = 'users'
urlpatterns = [
    path('index/',views.index,name='index'),
    re_path('user_register/$',views.user_register,name='user_register'),
    re_path('user_login/$',views.user_login,name='user_login'),
    re_path('user_logout/$',views.user_logout,name='user_logout'),
    re_path('user_active/(\w+)/$',views.user_active,name='user_active'),
    re_path('user_forget/$',views.user_forget,name='user_forget'),
    re_path('user_reset/(\w+)/$',views.user_reset,name='user_reset'),
]
