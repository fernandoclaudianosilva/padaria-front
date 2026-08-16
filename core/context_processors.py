from django.conf import settings
from .models import Location
from .forms import NewsletterForm


def site_context(request):
    """Global context available to every template: site name, nav locations, newsletter form."""
    return {
        'SITE_NAME': settings.SITE_NAME,
        'nav_locations': Location.objects.filter(active=True),
        'newsletter_form': NewsletterForm(),
    }
