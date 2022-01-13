from django.urls import path
from django.urls.resolvers import URLPattern
from .views import LunchList, LunchDetail

urlpatterns = [
    path('', LunchList.as_view(), name='lunch_list'),
    path('<int:pk>/', LunchDetail.as_view(), name='lunch_detail'),
]