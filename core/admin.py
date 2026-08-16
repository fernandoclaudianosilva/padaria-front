from django.contrib import admin
from .models import (
    Location, CakeFlavor, Recipe,
    CakeTastingRequest, ContactMessage, NewsletterSubscriber,
)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone', 'active')
    list_filter = ('active', 'city')
    search_fields = ('name', 'address_line', 'city', 'phone')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CakeFlavor)
class CakeFlavorAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_tasting_option', 'active', 'order')
    list_filter = ('is_tasting_option', 'active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('order',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'published', 'created_at')
    list_filter = ('featured', 'published')
    search_fields = ('title', 'description', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CakeTastingRequest)
class CakeTastingRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'preferred_date', 'guests', 'handled', 'created_at')
    list_filter = ('handled', 'preferred_date')
    search_fields = ('name', 'email', 'phone', 'message')
    list_editable = ('handled',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'handled', 'created_at')
    list_filter = ('handled',)
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('handled',)


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'active', 'created_at')
    list_filter = ('active',)
    search_fields = ('email',)
