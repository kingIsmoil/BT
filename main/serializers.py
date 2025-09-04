from rest_framework import serializers
from .models import Quote, Application
import re


class QuoteSerializer(serializers.ModelSerializer):
    tariff = serializers.ChoiceField(
        choices=["econom", "standart", "premium"]
    )
    car_type = serializers.ChoiceField(
        choices=["car", "truck", "moto"]
    )
    age = serializers.IntegerField(min_value=18)
    experience = serializers.IntegerField(min_value=0)

    class Meta:
        model = Quote
        fields = "__all__"
        read_only_fields = ["price", "created_at"]


    def validate(self, attrs):
        age = attrs.get("age")
        exp = attrs.get("experience")
        if exp > age:
            raise serializers.ValidationError(
                {"experience": "Стаж не может быть больше возраста."}
            )
        return attrs

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"

    def validate_phone(self, value):
        pattern = r"^\+992\d{9}$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Телефон должен быть в формате +992XXXXXXXXX (9 цифр после кода)."
            )
        return value

    def validate(self, attrs):
        if not attrs.get("quote"):
            raise serializers.ValidationError({"quote": "Quote обязателен."})
        return attrs
