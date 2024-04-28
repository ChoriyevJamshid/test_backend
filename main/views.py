from django.db.models import Prefetch, OuterRef, F, Value
from django.forms import IntegerField
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.contrib.postgres.expressions import ArraySubquery

from . import serializers
from . import models
from .models import Product, ProductMaterial


class ProductAPI(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


# @api_view(['GET', 'POST'])
# def response_view(request):
#
#     if request.method == 'POST':
#         return Response({'message': 'POST'})
#     else:
#         return Response({'message': 'GET'})


class RequestAPI(generics.CreateAPIView):
    serializer_class = serializers.RequestSerializer

    def post(self, request, *args, **kwargs):
        code = request.data['code']
        quantity = request.data['quantity']

        products = Product.objects.filter(code=code).annotate(
            quantity=Value(quantity)
        ).prefetch_related('materials', )

        serializer = serializers.ProductResultSerializer(instance=products, many=True)

        return Response({'result': serializer.data})

    def get(self, request):
        return Response({'message': 'GET'})


class ResultAPI(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductResultSerializer

    def get_queryset(self):
        print(self.request.data)
        return super().get_queryset()






