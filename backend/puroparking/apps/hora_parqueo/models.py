from django.db import models

class hora_parqueo(models.Model):

    precio = models.TextField("Precio")
    servicio_id = models.IntegerField("Servicio")

    def__str__(self):

    return f'{self.precio}'

    def__str__(self):
    return f'{self.servicio_id}'




