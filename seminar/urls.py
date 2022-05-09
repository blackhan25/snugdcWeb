# seminar/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import blogPosts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogPosts.views.index, name='index'),
    path('posts/', include('blogPosts.urls')),
]
