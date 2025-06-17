from django.db import models

class facturacion (models.Model):

    vehiculo_id = models.IntegerField("Vehiculo")
    total_pagar = models.TextField("Total a pagar")

    def__str__(self):

    return f'{self.vehiculo_id}'

    def__str__(self):

    return f'{self.total_pagar}'



