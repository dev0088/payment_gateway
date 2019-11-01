from django.conf.urls import url
from . import stripe_views

urlpatterns = [
    url(r'^checkout', stripe_views.StripePayment.as_view())
]
