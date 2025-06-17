from django.db import models

class vehiculo (models.Model):
    Placa = models.TextField("Placa")
    matricula_vehiculo = models.TextField("Matricula y vehiculo")
    usuario_id = models.IntegerField("Usuario")
    fecha_ingreso = models.TextField("Fecha de ingreso")
    Servicio_id = models.IntegerField("Servicio")


    def__str__(self):

    def __str__(self):
        return f'{self.Placa}'
    
    def __str__(self):
        return f'{self.matricula_vehiculo}'
    def __str__(self):
        return f'{self.usuario_id}'
    def __str__(self):
        return f'{self.fecha_ingreso}'
    def __str__(self):
        return f'{self.Servicio_id}'