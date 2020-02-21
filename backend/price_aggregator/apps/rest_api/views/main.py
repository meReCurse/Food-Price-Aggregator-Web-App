from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Shop, Product, ShopSerializer, ProductSerializer
from ..utils import Perekrestok_prices_receiver
# Create your views here.


class ProductsList(APIView):
    def post(self, request, format=None):
        product_name = request.data['name']
        result = Perekrestok_prices_receiver(product_name).received
        return Response(result)
