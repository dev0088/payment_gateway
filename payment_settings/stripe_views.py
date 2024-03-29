from django.shortcuts import render
from django.http import HttpResponse
from .models import StripeSetting
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .stripe_checkout_serializers import StripeCheckoutSerializer, StripeCheckoutResponseSerializer
import stripe
import requests
import json

test_credit_card_source = '4242424242424242'

class StripePayment(APIView):
    @swagger_auto_schema(
      request_body=StripeCheckoutSerializer,
      responses={200: StripeCheckoutResponseSerializer(many=False)}
    )
    def post(self, request, format=None):
        '''
        Checkout on Stripe payment
        '''
        stripe_setting = StripeSetting.objects.all().first()
        if stripe_setting is None:
          raise Response(
            data={
              'error': 'API gateway don\'t have any Stripe payment settings, yet. Please contact administrator.'
            },
            status=503
          )
        if stripe_setting.is_live_mode:
          stripe.api_key = stripe_setting.live_secret_key
        else:
          stripe.api_key = stripe_setting.test_secret_key
        stripe.log = 'info'  # or 'debug'

        request_data = request.data
        try:
          charge = stripe.Charge.create(
              amount=request_data['amount'],
              currency=request_data['currency'],
              source=request_data['source'],
              description=request_data['description'] if request_data['description'] else 'Nono application',
              statement_descriptor='22 Characters max',
              metadata={
                'email': request.data['email'],
                'telnumber': request.data['telnumber']
              }
          )

          # Only confirm an order after you have status: succeeded
          print('______STATUS_____', charge['status'])  # should be succeeded
          if charge['status'] == 'succeeded':
              return HttpResponse(json.dumps(
                  {
                    'status': 200,
                    'message': 'Your transaction has been successful.'
                  }
                )
              )
          else:
              raise stripe.error.CardError
        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            print('Status is: %s' % e.http_status)
            print('Type is: %s' % err.get('type'))
            print('Code is: %s' % err.get('code'))
            print('Message is %s' % err.get('message'))
            return HttpResponse(
                json.dumps({'status': 403, 'message': err.get('message')}),
                status=e.http_status
            )
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            return HttpResponse(json.dumps({
                'status': 403,
                'message': 'The API was not able to respond, try again.'
            }))
        except stripe.error.InvalidRequestError as e:
            # invalid parameters were supplied to Stripe's API
            return HttpResponse(json.dumps({
                'status': 404,
                'message': 'Invalid parameters, unable to process payment.'
            }))
        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            pass
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            return HttpResponse(json.dumps({
                'status': 408,
                'message': 'Network communication failed, try again.'
            }))
        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe
            # send yourself an email
            return HttpResponse(json.dumps({
                'status': 403,
                'message': 'Internal Error, contact support.'
            }))

        # Something else happened, completely unrelated to Stripe
        except Exception as e:
            return HttpResponse(json.dumps({
                'status': 403,
                'message': 'Unable to process payment, try again.'
            }))
