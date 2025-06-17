from django.db import models

class servicio (models.Model):

    nombre = models.TextField("Nombre")
    usuario_id = models.TextField("Usuario")
    placa_vehiculo = models.TextField("Placa de vehiculo")

    def__str__(self):

    return f'{self.nombre}'
    def__str__(self):

    return f'{self.usuario_id}'
    def__str__(self):
    
    return f'{self.placa_vehiculo}'


