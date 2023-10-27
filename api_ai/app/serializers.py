from rest_framework import serializers
from .models import Reports

class ReportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reports
        fields = ['pk', 'hacker_id', 'program_id', 'asset_id', 'vuln_id', 'severity' ,'rating', 'title', 'description', 'impact', 'status', 'created_at', 'updated_at']