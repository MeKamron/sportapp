from django.contrib import admin

from .models import SportTuri, SportCenter

admin.site.register(SportTuri)


@admin.register(SportCenter)
class SportCenterAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'sport_turi', 'manzil']