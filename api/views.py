from django.shortcuts import get_object_or_404
from django.db.models import Q
from .serializers import SportTuriSerializer, SportCenterSerializer
from main.models import SportTuri, SportCenter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal
import operator


@api_view(["GET"])
def SportTuriListApiView(request):
    turlar = SportTuri.objects.all()
    search = request.GET.get("search")
    if search:
        turlar = turlar = SportTuri.objects.filter(nomi__icontains=search)
    
    serializer = SportTuriSerializer(turlar, many=True)
    return Response(serializer.data, status=200)



@api_view(['GET'])
def SportTuriDetailApiView(request, pk):
    try:
        tur = get_object_or_404(SportTuri, pk=pk)
        serializer = SportTuriSerializer(tur)
        return Response(serializer.data, status=200)
    except:
        return Response({"error": "bunday ma`lumot mavjud emas"})


@api_view(["GET"])
def SportCentersListApiView(request):
    centers = SportCenter.objects.all()
    search = request.GET.get("search")
    if search:
        centers = SportCenter.objects.filter(Q(nomi__icontains=search) | Q(manzil__icontains=search))
    serializer = SportCenterSerializer(centers, many=True)
    return Response(serializer.data, status=200)



@api_view(['GET'])
def SportCenterDetailApiView(request, pk):
    try:
        center = get_object_or_404(SportCenter, pk=pk)
        serializer = SportCenterSerializer(center)
        return Response(serializer.data, status=200)
    except:
        return Response({"error": "bunday malumot mavjud emas"})


@api_view(['GET'])
def yaqinlik_boyicha_filter(request):
    location_results = {}
    if request.method == "GET":
        uzunlik = request.GET.get('uz')
        kenglik = request.GET.get('keng')
        user_location_sum = 0
        if uzunlik and kenglik:
            user_location_sum = Decimal(uzunlik) + Decimal(kenglik)   
        for center in SportCenter.objects.filter(is_active=True):
            center_location_sum = Decimal(center.latitude) + Decimal(center.longtitude)
            substraction = user_location_sum - center_location_sum
            if substraction < 0:
                substraction *= -1
            location_results[center.id] = substraction
        location_results = dict(sorted(location_results.items(), key=operator.itemgetter(1)))
        natijalar = [SportCenter.objects.get(id=int(id)) for id in location_results.keys()]
        serializer = SportCenterSerializer(natijalar, many=True)
        return Response(serializer.data)
    return Response({"error": "So'rovda xatolik bor!"})