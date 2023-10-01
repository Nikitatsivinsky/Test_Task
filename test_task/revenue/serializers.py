from rest_framework import serializers
from .models import RevenueStatistic

class RevenueStatisticSerializer(serializers.ModelSerializer):
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2, read_only=True)
    class Meta:
        model = RevenueStatistic
        fields = ('date', 'name', 'total_revenue',)