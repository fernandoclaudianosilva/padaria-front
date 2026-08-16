from decimal import Decimal
from django.test import TestCase
from django.urls import reverse

from .models import Category, Product


class ShopViewsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Cakes', slug='cakes')
        self.product = Product.objects.create(
            name='Chocolate Cake', slug='chocolate-cake', category=self.category,
            description='Rich chocolate cake.', short_description='Rich chocolate cake.',
            price=Decimal('32.00'), stock=5, active=True, featured=True,
        )

    def test_product_list(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chocolate Cake')

    def test_category_detail(self):
        response = self.client.get(reverse('shop:category_detail', args=['cakes']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chocolate Cake')

    def test_product_detail(self):
        response = self.client.get(reverse('shop:product_detail', args=['chocolate-cake']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '32.00')

    def test_inactive_product_not_listed(self):
        self.product.active = False
        self.product.save()
        response = self.client.get(reverse('shop:product_list'))
        self.assertNotContains(response, 'Chocolate Cake')
