from django.conf.urls import url
from . import square_views

urlpatterns = [
    url(r'^checkout', square_views.SquarePayment.as_view())
]
