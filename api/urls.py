from django.urls import path, include

from .views import AdminPaymentList, AdminDetailList, PublicPaymentList

urlpatterns = [
    path('admin/', AdminPaymentList.as_view()),
    path('admin/<int:pk>', AdminDetailList.as_view()),
    path('public/', PublicPaymentList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]