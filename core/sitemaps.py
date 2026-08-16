from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from shop.models import Product, Category
from .models import Recipe


class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return [
            'core:home', 'core:story', 'core:philosophy', 'core:locations',
            'core:contact', 'core:recipes', 'core:cake_tastings',
            'core:wedding_cakes', 'shop:product_list',
        ]

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Product.objects.filter(active=True)

    def lastmod(self, obj):
        return obj.updated_at


class CategorySitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return Category.objects.filter(active=True)


class RecipeSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return Recipe.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_at


sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'categories': CategorySitemap,
    'recipes': RecipeSitemap,
}
