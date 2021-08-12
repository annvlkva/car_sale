from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from car_sale_app.models import Car, Dealer
from car_sale_app.serializers import CarSerializer, DealerSerializer


class CarView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response({"cars": serializer.data})
    def post(self, request):
        car = request.data.get('car')
        serializer = CarSerializer(data=car)
        if serializer.is_valid(raise_exception=True):
            car_saved = serializer.save()
        return Response({"success": "Car '{}' created successfully".format(car_saved.vin)})

class CarIdView(APIView):
    def get(self, request, id):
        car = get_object_or_404(Car.objects.all(), id=id)
        serializer = CarSerializer(car)
        return Response({"car": serializer.data})
    def put(self, request, id):
        saved_car = get_object_or_404(Car.objects.all(), id=id)
        data = request.data.get('car')
        serializer = CarSerializer(instance=saved_car, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            car_saved = serializer.save()
        return Response({
            "success": "Car '{}' updated successfully".format(car_saved.id)
        })
    def delete(self, request, id):
        car = get_object_or_404(Car.objects.all(), id=id)
        car.delete()
        return Response({
            "message": "Car with id `{}` has been deleted.".format(id)
        }, status=204)

class DealerView(APIView):
    def get(self, request):
        dealers = Dealer.objects.all()
        serializer = DealerSerializer(dealers, many=True)
        return Response({"dealers": serializer.data})
    def post(self, request):
        dealer = request.data.get('dealer')
        serializer = DealerSerializer(data=dealer)
        if serializer.is_valid(raise_exception=True):
            dealer_saved = serializer.save()
        return Response({"success": "Dealer '{}' created successfully".format(dealer_saved.name)})

class DealerIdView(APIView):
    def get(self, request, id):
        dealer = get_object_or_404(Dealer.objects.all(), id=id)
        serializer = DealerSerializer(dealer)
        return Response({"dealer": serializer.data})
    def put(self, request, id):
        saved_dealer = get_object_or_404(Dealer.objects.all(), id=id)
        data = request.data.get('dealer')
        serializer = DealerSerializer(instance=saved_dealer, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            dealer_saved = serializer.save()
        return Response({
            "success": "Dealer '{}' updated successfully".format(dealer_saved.id)
        })
    def delete(self, request, id):
        dealer = get_object_or_404(Dealer.objects.all(), id=id)
        dealer.delete()
        return Response({
            "message": "Dealer with id `{}` has been deleted.".format(id)
        }, status=204)