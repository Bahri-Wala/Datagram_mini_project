from django.db import models
from chain.models import Chain

# Create your models here.
class Address(models.Model):
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}'

class Store(models.Model):
    name = models.CharField(max_length=50)
    # cle etrangere pour realiser une relation un-à-un avec la classe Address
    address = models.OneToOneField(Address, on_delete=models.RESTRICT)
    # chaque point de vente a une seule enseigne donc cette cle etrangere represente une relation un-à-plusieurs entre store et chain
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

