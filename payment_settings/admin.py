from django.contrib import admin
from .models import StripeSetting, SquarSetting

@admin.register(StripeSetting)
class StripeSettingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'is_live_mode','live_publishable_key', 'description', 'updated_at'
    )
    list_display_links = (
        'id', 'name', 'is_live_mode', 'live_publishable_key', 'description', 'updated_at'
    )
    list_filter = ('name', 'live_publishable_key')
    list_per_page = 25


@admin.register(SquarSetting)
class SquareSettingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'is_live_mode','access_token', 'description', 'updated_at'
    )
    list_display_links = (
        'id', 'name', 'is_live_mode', 'access_token', 'description', 'updated_at'
    )
    list_filter = ('name', 'access_token')
    list_per_page = 25
