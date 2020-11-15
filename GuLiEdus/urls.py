"""GuLiEdus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from users import views
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('captcha/', include('captcha.urls')),
    re_path('^$', views.index, name='index'),
    re_path('^users/', include('users.urls', namespace='users')),
    re_path('^courses/', include('courses.urls', namespace='courses')),
    re_path('^operations/', include('operations.urls', namespace='operations')),
    re_path('^orgs/', include('orgs.urls', namespace='orgs')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
