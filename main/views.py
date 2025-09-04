from rest_framework import generics, permissions
from .models import Quote, Application
from .serializers import QuoteSerializer, ApplicationSerializer


class QuoteCreateView(generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def perform_create(self, serializer):
        tariff_coeff = {"econom": 1.0, "standart": 1.2, "premium": 1.5}
        car_coeff = {"car": 1.0, "truck": 1.5, "moto": 1.3}

        tariff = serializer.validated_data["tariff"]
        age = serializer.validated_data["age"]
        exp = serializer.validated_data["experience"]
        car_type = serializer.validated_data["car_type"]

        base_price = 10000
        price = base_price * tariff_coeff.get(tariff, 1.0) * car_coeff.get(car_type, 1.0)

        if age < 25:
            price *= 1.3
        if exp > 5:
            price *= 0.9

        serializer.save(price=round(price, 2))


class QuoteDetailView(generics.RetrieveAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


# -------- Applications -------- #
class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetailView(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
