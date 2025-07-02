from django.db import models

class facturacion (models.Model):

    vehiculo_id = models.IntegerField("Vehiculo")
    total_pagar = models.IntegerField("Total a pagar")