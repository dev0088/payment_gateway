from django.shortcuts import render
from django.http import HttpResponse
from .models import SquarSetting
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .square_checkout_serializers import SquareCheckoutSerializer, SquareCheckoutResponseSerializer
import square
import requests
import json


class SquarePayment(APIView):
    @swagger_auto_schema(
      request_body=SquareCheckoutSerializer,
      responses={200: SquareCheckoutResponseSerializer(many=False)}
    )
    def post(self, request, format=None):
        '''
        Checkout on Square payment
        '''
        return HttpResponse(json.dumps(
            {
              'status': 200,
              'message': 'Your transaction has been successful.'
            }
          )
        )
