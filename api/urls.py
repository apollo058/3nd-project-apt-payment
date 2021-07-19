from django.urls import path
from django.urls.conf import include

urlpatterns = [
    # path('/admin', include('admin.urls')),
    path('/public', include('public.urls'))
]