from django.shortcuts import render
from .models import Reports
from rest_framework import generics
from .serializers import ReportsSerializer


class ReportsCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Reports.objects.all(),
    serializer_class = ReportsSerializer


class ReportsList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer

class ReportsDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
