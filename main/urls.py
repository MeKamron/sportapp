from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .views import (
    home,
    sport_turi_create,
    sport_center_create,
    sport_center_update,
    user_logout,
)

app_name = "main"

urlpatterns = [
    path('', home, name="home"),
    path('centers_by_category/<int:sport_turi_id>/', home, name="centers_by_category"),
    path('sport-turi-create/', sport_turi_create, name="sport_turi_create"),
    path('sport-center-create/', sport_center_create, name="sport_center_create"),
    path('sport-center-update/<int:id>/', sport_center_update, name="sport_center_update"),

    # auth views
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/',user_logout, name="logout"),
]
