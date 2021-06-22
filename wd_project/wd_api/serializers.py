#
from rest_framework import serializers
from .models import Zone, Report

class ZoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zone 
        fields = ['id', 'name', 'created', 'updated', 'geometry']

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report 
        fields = ['id', 'created', 'updated', 'waste_type','location','reported_by']