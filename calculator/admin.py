from django.contrib import admin
from .models import Security, SecurityPrice, SyntheticIndex


class SecurityAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight')
    search_fields = ('name', 'weight')


class SecurityPriceAdmin(admin.ModelAdmin):
    list_display = ('registered', 'security', 'price')
    search_fields = ('registered', 'security', 'price')


class SyntheticIndexAdmin(admin.ModelAdmin):
    list_display = ('calculated', 'price')
    search_fields = ('calculated', 'price')


admin.site.register(Security, SecurityAdmin)
admin.site.register(SecurityPrice, SecurityPriceAdmin)
admin.site.register(SyntheticIndex, SyntheticIndexAdmin)
