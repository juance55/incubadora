from django.db import models

class Registro(models.Model):
    # Campos de texto
    fecha = models.DateField()
    tiempo_encubacion = models.CharField(max_length=30)
    tasa_mortalidad = models.CharField(max_length=50)
    tasa_supervivencia = models.CharField(max_length=50)
    evaluar_raza = models.CharField(max_length=50)
    inversion = models.CharField(max_length=50)

    class Meta:
        db_table = 'registro'
