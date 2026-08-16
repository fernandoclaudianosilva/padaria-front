from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('our-story/', views.story, name='story'),
    path('our-philosophy/', views.philosophy, name='philosophy'),
    path('locations/', views.locations, name='locations'),
    path('contact/', views.contact, name='contact'),
    path('cake-tastings/', views.cake_tastings, name='cake_tastings'),
    path('wedding-cakes/', views.wedding_cakes, name='wedding_cakes'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('order-online/', views.order_online, name='order_online'),
    path('search/', views.search, name='search'),
    path('newsletter/signup/', views.newsletter_signup, name='newsletter_signup'),
]
