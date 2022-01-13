from rest_framework import generics
from .models import Lunch
from .serializers import LunchSerializer
from .permissions import IsCreatorOrReadOnly

class LunchList(generics.ListCreateAPIView):
    queryset = Lunch.objects.all()
    serializer_class = LunchSerializer

class LunchDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCreatorOrReadOnly,)
    queryset = Lunch.objects.all()
    serializer_class = LunchSerializer



