from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from store.models import Store
import time
import random


# generer un code unique
def generate_code():
    while True:
        code = random.randint(10000000000, 99999999999)
        if Product.objects.filter(code=code).count() == 0:
            break
    return code


# Create your models here.
class Product(models.Model):
    # code est l'identificateur du modele(généré automatiquement)
    code = models.PositiveBigIntegerField(primary_key=True, blank=True)
    # barcode est une image généré automatiquement à partir du code at country_id et qui sera telechargé vers media/images
    barcode = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=3, max_digits=20)
    country_id = models.PositiveSmallIntegerField(validators=[MaxValueValidator(9)])
    #chaque produit a un seul store donc on a la relation un-à-plusieurs
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # cette methode permet de generer un code unique et l'image barcode du produit avant qu'il soit sauvegardé dans la bd
    def save(self, *args, **kwargs):
        self.code = generate_code()
        ean = barcode.get_barcode_class('ean13')
        code = ean(f'{self.country_id}{self.code}', writer=ImageWriter())
        buffer = BytesIO()
        code.write(buffer)
        self.barcode.save(str(time.time() * 1000)+'barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)


