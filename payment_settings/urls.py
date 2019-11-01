from django.conf.urls import include, url
from . import stripe_views

urlpatterns = [
    url(r'^stripe/', include('payment_settings.stripe_urls')),
    url(r'^square/', include('payment_settings.square_urls')),
]
