from django.shortcuts import render
from rest_framework import viewsets

from app.category.models import Category
from app.category.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
