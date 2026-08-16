from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from shop.models import Product, Category
from .models import Location, CakeFlavor, Recipe
from .forms import CakeTastingRequestForm, ContactForm, NewsletterForm


def home(request):
    categories = Category.objects.filter(active=True)[:8]
    featured_products = Product.objects.filter(active=True, featured=True)[:6]
    best_sellers = Product.objects.filter(active=True, best_seller=True)[:4]
    cake_flavors = CakeFlavor.objects.filter(active=True)[:8]
    recipes = Recipe.objects.filter(published=True, featured=True)[:3]
    locations = Location.objects.filter(active=True)
    context = {
        'categories': categories,
        'featured_products': featured_products,
        'best_sellers': best_sellers,
        'cake_flavors': cake_flavors,
        'recipes': recipes,
        'locations': locations,
        'page_title': "Gerardo's Italian Bakery | Authentic Italian Baking",
        'meta_description': "Gerardo's Italian Bakery — authentic Italian baking made with "
                             "passion since 1993. Wedding cakes, Italian cookies, cannoli, "
                             "pastries, breads and coffee across Massachusetts.",
    }
    return render(request, 'core/home.html', context)


def story(request):
    context = {
        'page_title': "Our Story | Gerardo's Italian Bakery",
        'meta_description': "The story of Gerardo's Italian Bakery, founded in 1993 by "
                             "Gerardo Sarli, built on family recipes and Italian tradition.",
    }
    return render(request, 'core/story.html', context)


def philosophy(request):
    context = {
        'page_title': "Our Philosophy | Gerardo's Italian Bakery",
    }
    return render(request, 'core/philosophy.html', context)


def locations(request):
    context = {
        'locations': Location.objects.filter(active=True),
        'page_title': "Locations | Gerardo's Italian Bakery",
        'meta_description': "Visit Gerardo's Italian Bakery in West Boylston, Marlborough "
                             "and Shrewsbury, Massachusetts.",
    }
    return render(request, 'core/locations.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your message has been sent — we'll be in touch soon.")
            return redirect('core:contact')
    else:
        form = ContactForm()
    context = {
        'form': form,
        'locations': Location.objects.filter(active=True),
        'page_title': "Contact | Gerardo's Italian Bakery",
    }
    return render(request, 'core/contact.html', context)


def cake_tastings(request):
    if request.method == 'POST':
        form = CakeTastingRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! We've received your tasting request and will reach out shortly.")
            return redirect('core:cake_tastings')
    else:
        form = CakeTastingRequestForm()
    context = {
        'form': form,
        'flavors': CakeFlavor.objects.filter(active=True, is_tasting_option=True),
        'page_title': "Cake Tastings | Gerardo's Italian Bakery",
        'meta_description': "Book a cake tasting at Gerardo's Italian Bakery and sample "
                             "flavors for your wedding cake or special event.",
    }
    return render(request, 'core/cake_tastings.html', context)


def wedding_cakes(request):
    context = {
        'flavors': CakeFlavor.objects.filter(active=True),
        'page_title': "Wedding Cakes | Gerardo's Italian Bakery",
        'meta_description': "Custom Italian wedding cakes from Gerardo's Italian Bakery, "
                             "recognized as Best of New England by The Knot.",
    }
    return render(request, 'core/wedding_cakes.html', context)


def recipes(request):
    context = {
        'recipes': Recipe.objects.filter(published=True),
        'page_title': "From Our Kitchen | Gerardo's Italian Bakery",
    }
    return render(request, 'core/recipes.html', context)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, published=True)
    related = Recipe.objects.filter(published=True).exclude(pk=recipe.pk)[:3]
    context = {
        'recipe': recipe,
        'related': related,
        'page_title': f"{recipe.title} | Gerardo's Italian Bakery",
    }
    return render(request, 'core/recipe_detail.html', context)


def order_online(request):
    context = {
        'locations': Location.objects.filter(active=True).exclude(order_online_url=''),
        'page_title': "Order Online | Gerardo's Italian Bakery",
    }
    return render(request, 'core/order_online.html', context)


def search(request):
    query = request.GET.get('q', '').strip()
    products = Product.objects.none()
    categories = Category.objects.none()
    recipe_results = Recipe.objects.none()

    if query:
        products = Product.objects.filter(
            Q(active=True) & (Q(name__icontains=query) | Q(description__icontains=query))
        )
        categories = Category.objects.filter(
            Q(active=True) & (Q(name__icontains=query) | Q(description__icontains=query))
        )
        recipe_results = Recipe.objects.filter(
            Q(published=True) & (Q(title__icontains=query) | Q(description__icontains=query))
        )

    context = {
        'query': query,
        'products': products,
        'categories': categories,
        'recipes': recipe_results,
        'result_count': products.count() + categories.count() + recipe_results.count(),
        'page_title': f"Search results for \"{query}\"" if query else "Search",
    }
    return render(request, 'core/search.html', context)


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You're on the list! Thanks for signing up.")
        else:
            messages.error(request, "Please enter a valid email address.")
    return redirect(request.META.get('HTTP_REFERER', 'core:home'))
