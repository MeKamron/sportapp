from django.contrib import auth
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from .models import SportTuri, SportCenter
from .forms import (
    SearchForm, 
    SportTuriCreateForm,
    SportCenterCreateForm,
)


def PagenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')

    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


@login_required
def home(request, sport_turi_id=None):
    turlar = SportTuri.objects.all()
    centers = SportCenter.objects.all()
    sport_turi=None
    if sport_turi_id:
        sport_turi = get_object_or_404(SportTuri,id=sport_turi_id)
        centers = sport_turi.sport_centers.all()
    
    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            cd = search_form.cleaned_data
            centers = centers.filter(Q(nomi__icontains=cd['q']) | Q(manzil__icontains=cd['q']))
    else:
        search_form = SearchForm()
    sport_turi_create_form = SportTuriCreateForm()
    sport_center_create_form = SportCenterCreateForm()
    page = request.GET.get('page')
    context = {
        "turlar": turlar,
        "centers": PagenatorPage(centers, 15, request),
        "page": page,
        "sport_turi": sport_turi,
        "search_form": search_form,
        "sport_turi_create_form": sport_turi_create_form,
        "sport_center_create_form": sport_center_create_form,
    }
    return render(request, "main/home.html", context)


@login_required
def sport_center_update(request, id):
    center = get_object_or_404(SportCenter, id=id)
    if request.method == "POST":
        form = SportCenterCreateForm(request.POST, request.FILES, instance=center)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    else:
        form = SportCenterCreateForm(instance=center)
    return render(request, "main/update.html", {"form": form, "center": center})



@login_required
def sport_turi_create(request):
    if request.method == "POST":
        form = SportTuriCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return redirect("/")

@login_required
def sport_center_create(request):
    if request.method == "POST":
        form = SportCenterCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"/centers_by_category/{form.cleaned_data['sport_turi'].id}")
        else:
            return redirect(f"/")


def user_logout(request):
    logout(request)
    return render(request, "registration/logout.html")
