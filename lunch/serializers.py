from rest_framework import serializers
from .models import Lunch

class LunchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'customer', 'name', 'description', 'price', 'category', 'rating')
        model = Lunch