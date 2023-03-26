from rest_framework import viewsets
from .serializers import CurrencySerializer
from .models import Currency

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
