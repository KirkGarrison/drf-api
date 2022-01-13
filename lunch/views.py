from rest_framework import generics
from .models import Lunch
from .serializers import LunchSerializer

class LunchList(generics.ListCreateAPIView):
    queryset = Lunch.objects.all()
    serializer_class = LunchSerializer

class LunchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lunch.objects.all()
    serializer_class = LunchSerializer



