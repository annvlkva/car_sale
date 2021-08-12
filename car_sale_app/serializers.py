from rest_framework import serializers
from car_sale_app.models import Car, Dealer

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    vin = serializers.CharField(max_length=17)
    make = serializers.CharField()
    model = serializers.CharField()
    year = serializers.IntegerField()
    dealer_id = serializers.IntegerField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.vin = validated_data.get('vin', instance.vin)
        instance.make = validated_data.get('make', instance.make)
        instance.model = validated_data.get('model', instance.model)
        instance.year = validated_data.get('year', instance.year)
        instance.dealer_id = validated_data.get('dealer_id', instance.dealer_id)
        instance.save()
        return instance

class DealerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    phone = serializers.CharField(max_length=11)
    address = serializers.CharField()

    def create(self, validated_data):
        return Dealer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance