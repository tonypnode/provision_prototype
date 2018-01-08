from django.contrib import admin
from django.urls import path, re_path
from auto_config.views import home, new_provision


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', home),
    re_path(r'new/$', new_provision),
]
