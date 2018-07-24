"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^files/', views.files, name='files'),
    url(r'^grades/', views.grades, name='grades'),
    url(r'^small_multiples_files_bar_chart/', views.small_multiples_files_bar_chart, name='small_multiples_files_bar_chart'),

    # get file access patterns
    url(r'^file_access', views.file_access, name='file_access'),

    # load file information
    url(r'^load_data', views.load_data, name='load_data'),

    url(r'^$', serve, {
        'path': '/home.html',
        'document_root': '.',
    }),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)