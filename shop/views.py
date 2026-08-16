from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Product


def product_list(request):
    products = Product.objects.filter(active=True)
    categories = Category.objects.filter(active=True)

    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    sort = request.GET.get('sort')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')

    paginator = Paginator(products, 12)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'categories': categories,
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'active_category': category_slug,
        'page_title': "Shop | Gerardo's Italian Bakery",
        'meta_description': "Shop breads, cakes, pastries, cannoli, cookies, wedding "
                             "cakes and coffee from Gerardo's Italian Bakery.",
    }
    return render(request, 'shop/products.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug, active=True)
    products = category.products.filter(active=True)

    paginator = Paginator(products, 12)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'category': category,
        'categories': Category.objects.filter(active=True),
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'page_title': f"{category.name} | Gerardo's Italian Bakery",
        'meta_description': category.description or f"Shop {category.name} from Gerardo's Italian Bakery.",
    }
    return render(request, 'shop/category.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, active=True)
    related_products = Product.objects.filter(
        category=product.category, active=True
    ).exclude(pk=product.pk)[:4]

    context = {
        'product': product,
        'related_products': related_products,
        'page_title': f"{product.name} | Gerardo's Italian Bakery",
        'meta_description': product.short_description or product.description[:160],
    }
    return render(request, 'shop/product_detail.html', context)
