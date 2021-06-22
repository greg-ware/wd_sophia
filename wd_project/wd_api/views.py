from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Zone, Report
from rest_framework import generics, serializers
from .serializers import ZoneSerializer, ReportSerializer

## Zones API
class ZoneListCreate(generics.ListCreateAPIView):
    # API endpoint that allows creation of a new zone
    queryset = Zone.objects.all(),
    serializer_class = ZoneSerializer
    lookup_field='id'

class ZoneList(generics.ListAPIView):
    # API endpoint that allows zones to be listed.
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    lookup_field='id'

class ZoneCreate(generics.CreateAPIView):
    # API endpoint that allows zones to be listed.
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    lookup_field='id'

class ZoneDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single zone by id.
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    lookup_field='id'

class ZoneUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that returns a single zone by id.
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    lookup_field='id'

class ZoneDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that returns a single zone by id.
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    lookup_field='id'

class ZoneRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # API endpoint that returns a single report by id.
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    lookup_field='id'

## Reports API

class ReportListCreate(generics.ListCreateAPIView):
    # API endpoint that allows creation of a new report
    queryset = Report.objects.all(),
    serializer_class = ReportSerializer
    lookup_field='id'

class ReportList(generics.ListAPIView):
    # API endpoint that allows creation of a new report
    queryset = Report.objects.all(),
    serializer_class = ReportSerializer
    lookup_field='id'

class ReportCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new report
    queryset = Report.objects.all(),
    serializer_class = ReportSerializer
    lookup_field='id'


class ReportRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # API endpoint that returns a single report by id.
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field='id'
