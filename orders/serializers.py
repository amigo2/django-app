from rest_framework import serializers

from core.models import Order



class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields= ('id', 'name', 'date', 'amount')
        read_only_fields = ('id',)

class OrderDetailSerializer(serializers.ModelSerializer):

    order = OrderSerializer(many=True, read_only=True)