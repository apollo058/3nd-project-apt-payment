from .serializer import PaymentSerializer
from .models     import Payment

from rest_framework             import generics
from rest_framework.permissions import IsAdminUser

class AdminPaymentList(generics.ListCreateAPIView):
        queryset           = Payment.objects.all()
        serializer_class   = PaymentSerializer
        permission_classes = [IsAdminUser]

class AdminDetailList(generics.RetrieveUpdateDestroyAPIView):
        queryset           = Payment.objects.all()
        serializer_class   = PaymentSerializer
        permission_classes = [IsAdminUser]

class PublicPaymentList(generics.ListAPIView):
        serializer_class = PaymentSerializer

        def get_queryset(self):
                user = self.request.user
                return Payment.objects.filter(name=user.username)
