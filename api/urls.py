from django.urls import path
from .views import (
    SportTuriListApiView,
    SportTuriDetailApiView,
    SportTuriDetailApiView, 
    SportCentersListApiView,
    yaqinlik_boyicha_filter
)

urlpatterns = [
    path('turlar/', SportTuriListApiView),
    path('turlar/<int:pk>/', SportTuriDetailApiView),
    path('centerlar/', SportCentersListApiView),
    path('centerlar/<int:pk>/', SportTuriDetailApiView),
    path('centerlar/filter/', yaqinlik_boyicha_filter),
]