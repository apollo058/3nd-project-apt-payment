from django.contrib.auth.models import User

from .serializer import PaymentSerializer
from .models     import Payment

from rest_framework             import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class AdminPaymentList(generics.ListCreateAPIView):
        authentication_classes = [SessionAuthentication]
        permission_classes     = [IsAdminUser]
        queryset               = Payment.objects.all()
        serializer_class       = PaymentSerializer


class AdminDetailList(generics.RetrieveUpdateDestroyAPIView):
        authentication_classes = [SessionAuthentication]
        permission_classes     = [IsAdminUser]
        queryset               = Payment.objects.all()
        serializer_class       = PaymentSerializer

class PublicPaymentList(generics.ListAPIView):
        authentication_classes = [SessionAuthentication]
        permission_classes     = [IsAuthenticated]
        serializer_class       = PaymentSerializer

        def get_queryset(self):
                user = self.request.user
                return user.payment_set.all()