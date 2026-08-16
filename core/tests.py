from django.test import TestCase
from django.urls import reverse

from .models import Location, Recipe, CakeFlavor
from shop.models import Category, Product


class CoreViewsTests(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            name="Gerardo's Italian Bakery - West Boylston",
            slug='west-boylston',
            address_line='339 West Boylston St.',
            city='West Boylston',
            state='MA',
            phone='508-853-3434',
            hours='Sunday-Wednesday: 8:00 am - 8:00 pm',
        )
        self.category = Category.objects.create(name='Cannoli', slug='cannoli')
        self.product = Product.objects.create(
            name='Classic Cannoli', slug='classic-cannoli', category=self.category,
            description='A crisp shell filled with sweet ricotta.',
            short_description='A taste of Italy.', price='4.50', stock=10, active=True,
        )
        self.recipe = Recipe.objects.create(
            title='How We Make Cannoli Shells', slug='cannoli-shells',
            description='A peek behind the scenes.', content='Full story here.',
            published=True,
        )

    def test_home_page(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gerardo")

    def test_locations_page(self):
        response = self.client.get(reverse('core:locations'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'West Boylston')

    def test_contact_page_get(self):
        response = self.client.get(reverse('core:contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_form_submit(self):
        response = self.client.post(reverse('core:contact'), {
            'name': 'Test User', 'email': 'test@example.com', 'phone': '',
            'subject': 'Hello', 'message': 'A test message.',
        })
        self.assertEqual(response.status_code, 302)

    def test_cake_tasting_page(self):
        response = self.client.get(reverse('core:cake_tastings'))
        self.assertEqual(response.status_code, 200)

    def test_cake_tasting_form_submit(self):
        response = self.client.post(reverse('core:cake_tastings'), {
            'name': 'Bride To Be', 'email': 'bride@example.com', 'phone': '',
            'guests': 2, 'message': 'Looking forward to it!',
        })
        self.assertEqual(response.status_code, 302)

    def test_wedding_cakes_page(self):
        response = self.client.get(reverse('core:wedding_cakes'))
        self.assertEqual(response.status_code, 200)

    def test_recipes_list_and_detail(self):
        response = self.client.get(reverse('core:recipes'))
        self.assertEqual(response.status_code, 200)
        detail = self.client.get(reverse('core:recipe_detail', args=[self.recipe.slug]))
        self.assertEqual(detail.status_code, 200)

    def test_search(self):
        response = self.client.get(reverse('core:search'), {'q': 'cannoli'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Classic Cannoli')

    def test_newsletter_signup(self):
        response = self.client.post(
            reverse('core:newsletter_signup'),
            {'email': 'fan@example.com'},
            HTTP_REFERER='/',
        )
        self.assertEqual(response.status_code, 302)
