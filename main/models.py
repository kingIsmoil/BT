from django.db import models
from django.conf import settings


class Quote(models.Model):
    TARIFF_CHOICES = [
        ("econom", "Эконом"),
        ("standart", "Стандарт"),
        ("premium", "Премиум"),
    ]

    CAR_CHOICES = [
        ("car", "Легковой"),
        ("truck", "Грузовой"),
        ("moto", "Мото"),
    ]

    tariff = models.CharField(max_length=20, choices=TARIFF_CHOICES)
    age = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    car_type = models.CharField(max_length=20, choices=CAR_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tariff} - {self.car_type} - {self.price}"



class Application(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    tariff = models.CharField(max_length=100)               
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application #{self.id} — {self.full_name}"
