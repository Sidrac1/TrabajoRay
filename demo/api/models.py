from django.db import models

from django.contrib.auth.models import User

class Bank(models.Model):
    name = models.CharField(max_length=32, default='Generic Bank Name')
    address = models.CharField(max_length=64, default='Generic Bank Address')
    status = models.BooleanField(default=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    update = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

CURRENCY_CHOICES = (
    ('MXN', 'Peso Mexicano'),
    ('USD', 'Dolar americano'),
    ('EUR', 'Euro'),
)

class Account(models.Model):
    name = models.CharField(max_length=32, default='Generic Account Name')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=16, choices=CURRENCY_CHOICES)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    update = models.DateField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name





