from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method
from .models import *

class SquareCheckoutSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)
    base_price_money_amount = serializers.IntegerField(required=True)
    base_price_money_currency = serializers.CharField(required=True)
    discounts_name = serializers.CharField(required=True)
    discounts_percentage = serializers.CharField(required=True)
    taxes_name = serializers.CharField(required=True)
    taxes_percentage = serializers.CharField(required=True)
    merchant_support_email = serializers.CharField(required=True)
    pre_populate_buyer_email = serializers.CharField(required=True)
    shipping_address_line1 = serializers.CharField(required=True)
    shipping_address_line2 = serializers.CharField(required=True)
    shipping_address_locality = serializers.CharField(required=True)
    shipping_address_administrative_district_level_1 = serializers.CharField(required=True)
    shipping_address_postal_code = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    recipients_location_id = serializers.CharField(required=True)
    recipients_location_description = serializers.CharField(required=True)


class SquareCheckoutResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.ListField()
