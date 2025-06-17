from django.db import models
class rol (models.Model):

    nombre = models.TextField("Nombre")

    def__str__(self):

    return f'{self.nombre}'



