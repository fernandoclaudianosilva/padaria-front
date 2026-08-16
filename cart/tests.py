from decimal import Decimal
from django.test import TestCase
from django.urls import reverse

from shop.models import Category, Product


class CartTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Breads', slug='breads')
        self.product = Product.objects.create(
            name='Italian Loaf', slug='italian-loaf', category=category,
            description='Crusty artisan bread.', price=Decimal('6.50'),
            stock=20, active=True,
        )

    def test_add_to_cart(self):
        response = self.client.post(
            reverse('cart:cart_add', args=[self.product.id]), {'quantity': 2}
        )
        self.assertEqual(response.status_code, 302)
        detail = self.client.get(reverse('cart:cart_detail'))
        self.assertContains(detail, 'Italian Loaf')

    def test_cart_total(self):
        self.client.post(reverse('cart:cart_add', args=[self.product.id]), {'quantity': 3})
        detail = self.client.get(reverse('cart:cart_detail'))
        self.assertContains(detail, '19.50')

    def test_remove_from_cart(self):
        self.client.post(reverse('cart:cart_add', args=[self.product.id]), {'quantity': 1})
        self.client.post(reverse('cart:cart_remove', args=[self.product.id]))
        detail = self.client.get(reverse('cart:cart_detail'))
        self.assertNotContains(detail, 'Italian Loaf')

    def test_checkout_requires_items(self):
        response = self.client.get(reverse('cart:checkout'))
        self.assertEqual(response.status_code, 302)

    def test_checkout_flow(self):
        self.client.post(reverse('cart:cart_add', args=[self.product.id]), {'quantity': 1})
        response = self.client.post(reverse('cart:checkout'), {
            'first_name': 'Maria', 'last_name': 'Rossi', 'email': 'maria@example.com',
            'phone': '508-555-0100', 'address': '1 Main St', 'city': 'Worcester',
            'state': 'MA', 'zip_code': '01602', 'notes': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thank you')
