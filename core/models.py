from django.db import models
from django.urls import reverse


class Location(models.Model):
    """One of Gerardo's Italian Bakery physical storefronts."""
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)
    address_line = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, default='MA')
    zip_code = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=30)
    manager = models.CharField(max_length=120, blank=True)
    hours = models.TextField(
        help_text="Free-form opening hours, one line per day range, "
                   "e.g. 'Sunday-Wednesday: 8:00 am - 8:00 pm'."
    )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='locations/', blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    order_online_url = models.URLField(blank=True, help_text="Grubhub (or other) ordering link, if available.")
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:locations') + f'#{self.slug}'


class CakeFlavor(models.Model):
    """Cake flavor offered for custom cakes / wedding cakes / tastings."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cake_flavors/', blank=True, null=True)
    is_tasting_option = models.BooleanField(
        default=False,
        help_text="Show this flavor on the Cake Tastings page."
    )
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Editorial content: recipes, stories & inspiration from the bakery kitchen."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(help_text="Short teaser shown on listing cards.")
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    content = models.TextField(help_text="Full article body. Supports basic HTML.")
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:recipe_detail', args=[self.slug])


class CakeTastingRequest(models.Model):
    """Submissions from the Cake Tastings request form."""
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    preferred_date = models.DateField(blank=True, null=True)
    guests = models.PositiveIntegerField(blank=True, null=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Cake Tasting Request"
        verbose_name_plural = "Cake Tasting Requests"

    def __str__(self):
        return f"{self.name} ({self.created_at:%Y-%m-%d})"


class ContactMessage(models.Model):
    """Submissions from the general Contact form."""
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject or 'General inquiry'}"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email
