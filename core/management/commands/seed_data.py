from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from core.models import Location, CakeFlavor, Recipe
from shop.models import Category, Product


class Command(BaseCommand):
    help = "Seed the database with Gerardo's Italian Bakery starter content (locations, categories, cake flavors, sample products, recipes)."

    def handle(self, *args, **options):
        self.seed_locations()
        self.seed_categories()
        self.seed_cake_flavors()
        self.seed_products()
        self.seed_recipes()
        self.stdout.write(self.style.SUCCESS('Gerardo\'s Italian Bakery starter data created.'))

    def seed_locations(self):
        locations = [
            {
                'name': "Gerardo's Italian Bakery - West Boylston",
                'address_line': '339 West Boylston St.',
                'city': 'West Boylston',
                'phone': '508-853-3434',
                'hours': (
                    'Sunday-Wednesday: 8:00 am - 8:00 pm\n'
                    'Thursday-Saturday: 8:00 am - 9:00 pm'
                ),
                'description': 'One of three Gerardo\'s Italian Bakery locations in Massachusetts.',
                'order_online_url': '',
            },
            {
                'name': "Gerardo's Bakery - Marlborough",
                'address_line': '115 Apex Dr',
                'city': 'Marlborough',
                'phone': '(508) 251-0234',
                'hours': (
                    'Sunday-Thursday: 10:00 am - 8:00 pm\n'
                    'Friday-Saturday: 10:00 am - 8:00 pm'
                ),
                'description': 'One of three Gerardo\'s Italian Bakery locations in Massachusetts.',
                'order_online_url': '',
            },
            {
                'name': "Gerardo's Italian Bakery - Shrewsbury",
                'address_line': '97 Turnpike Rd.',
                'city': 'Shrewsbury',
                'phone': '1-508-925-5151',
                'hours': (
                    'Monday-Saturday: 8:00 am - 9:00 pm\n'
                    'Sunday: 8:00 am - 8:00 pm'
                ),
                'description': 'One of three Gerardo\'s Italian Bakery locations in Massachusetts.',
                'order_online_url': '',
            },
        ]
        for data in locations:
            Location.objects.get_or_create(slug=slugify(data['name']), defaults={**data, 'state': 'MA'})
        self.stdout.write('Locations ready.')

    def seed_categories(self):
        categories = [
            ('Breads', 'Traditional Italian breads, baked fresh every day.'),
            ('Pastries', 'Italian pastries made the traditional way.'),
            ('Cakes', 'Cakes for every occasion, from a simple slice to a celebration centerpiece.'),
            ('Cannoli', 'A taste of Italy — crisp shells, filled to order.'),
            ('Cookies', 'Italian cookies made to share.'),
            ('Wedding Cakes', 'Custom wedding cakes, tasted and designed with you.'),
            ('Coffee', 'Coffee, cappuccino and espresso.'),
            ('Special Events', 'Baked goods and treats for parties and special events.'),
        ]
        for order, (name, description) in enumerate(categories):
            Category.objects.get_or_create(
                slug=slugify(name),
                defaults={'name': name, 'description': description, 'order': order},
            )
        self.stdout.write('Categories ready.')

    def seed_cake_flavors(self):
        flavors = [
            ('Chocolate', 'Rich chocolate cake.', False),
            ('Vanilla', 'Classic white/vanilla cake.', False),
            ('Gold / Light Lemon', 'A light, gently citrus cake.', False),
            ('Marble', 'A swirl of chocolate and vanilla.', False),
            ('Carrot', 'A moist, spiced carrot cake.', False),
            ('Red Velvet', 'Rich, moist and flavorful.', False),
            ('Tiramisu', 'Inspired by the classic Italian dessert.', False),
            ('Rum Cake', 'A traditional Italian favorite.', False),
            ('Ricotta & Strawberry', 'A tasting favorite, filled with sweet ricotta and strawberry.', True),
            ('Cannoli Cake Filling', 'Our cannoli filling, baked into the cake.', True),
            ('Creamy Italian Mascarpone', 'A smooth, creamy mascarpone filling.', True),
            ('Raspberry Chambord', 'Raspberry filling with a touch of Chambord.', True),
            ('Strawberry Chiffon', 'A light strawberry chiffon filling.', True),
        ]
        for order, (name, description, is_tasting) in enumerate(flavors):
            CakeFlavor.objects.get_or_create(
                slug=slugify(name),
                defaults={
                    'name': name, 'description': description,
                    'is_tasting_option': is_tasting, 'order': order,
                },
            )
        self.stdout.write('Cake flavors ready.')

    def seed_products(self):
        cat = {c.slug: c for c in Category.objects.all()}

        def make(name, category_slug, price, short_description, description='', **extra):
            Product.objects.get_or_create(
                slug=slugify(name),
                defaults={
                    'name': name,
                    'category': cat[category_slug],
                    'price': Decimal(price),
                    'short_description': short_description,
                    'description': description or short_description,
                    'stock': 25,
                    'active': True,
                    **extra,
                },
            )

        make('Italian Semolina Loaf', 'breads', '6.50', 'Traditional crusty Italian bread.', featured=True, best_seller=True)
        make('Ciabatta', 'breads', '5.75', 'Light, airy, open-crumb loaf.')
        make('Sfogliatelle', 'pastries', '4.25', 'Flaky, shell-shaped Italian pastry.', featured=True)
        make('Baba au Rhum', 'pastries', '4.75', 'Rum-soaked Italian sponge pastry.')
        make('Chocolate Layer Cake', 'cakes', '32.00', 'Rich chocolate cake, whole size.', featured=True, best_seller=True)
        make('Tiramisu Cake', 'cakes', '34.00', 'Inspired by the classic Italian dessert.', featured=True)
        make('Classic Cannoli', 'cannoli', '4.50', 'Crisp shell, filled to order with sweet ricotta.', best_seller=True, featured=True)
        make('Chocolate Chip Cannoli', 'cannoli', '4.75', 'Classic cannoli filling with mini chocolate chips.')
        make('Italian Butter Cookies', 'cookies', '14.00', 'Assorted Italian butter cookies, sold by the pound.', best_seller=True)
        make('Pignoli Cookies', 'cookies', '16.00', 'Traditional almond cookies rolled in pine nuts.', featured=True)
        make('Custom Wedding Cake Consultation', 'wedding-cakes', '0.00', 'Start planning your wedding cake with our team.')
        make('Espresso', 'coffee', '3.00', 'Traditional Italian espresso.')
        make('Cappuccino', 'coffee', '4.00', 'Espresso with steamed, foamed milk.')
        make('Party Cookie Tray', 'special-events', '28.00', 'An assortment of Italian cookies for your next event.')
        self.stdout.write('Sample products ready.')

    def seed_recipes(self):
        recipes = [
            {
                'title': 'A Look Inside Our Cannoli Kitchen',
                'description': 'How our bakers fill each cannoli shell to order, every single day.',
                'content': (
                    'Every cannoli that leaves our bakery is filled to order, so the shell stays '
                    'crisp until the moment you take your first bite. It is a small detail, and one '
                    'our bakers have kept since the very beginning.'
                ),
                'featured': True,
            },
            {
                'title': 'Planning Your Wedding Cake Tasting',
                'description': 'What to expect when you sit down for a tasting with our cake team.',
                'content': (
                    'A cake tasting is where your wedding cake really begins. Our team walks you '
                    'through our most requested fillings, from creamy mascarpone to raspberry '
                    'Chambord, so you can choose the combination that fits your celebration.'
                ),
                'featured': True,
            },
            {
                'title': 'The Story Behind Our Family Recipes',
                'description': 'A short history of the Italian recipes that shaped our bakery.',
                'content': (
                    'Long before Gerardo\'s Italian Bakery opened its doors, its recipes were '
                    'already part of a family story — passed down and carried across the ocean '
                    'from Italy.'
                ),
                'featured': False,
            },
        ]
        for data in recipes:
            Recipe.objects.get_or_create(slug=slugify(data['title']), defaults=data)
        self.stdout.write('Recipes ready.')
