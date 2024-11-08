from django.db import models

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_comuna

class Particula(models.Model):
    id_particula = models.AutoField(primary_key=True)
    nombre_particula = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_particula

class Sensor(models.Model):
    id_sensor = models.AutoField(primary_key=True)
    nombre_sensor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_sensor

class ComunaSensor(models.Model):
    id_sensor_comuna = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comuna {self.comuna.nombre_comuna} - Sensor {self.sensor.nombre_sensor}"



class SensorParticula(models.Model):
    id_sensor_particula = models.AutoField(primary_key=True)
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    particula = models.ForeignKey('Particula', on_delete=models.CASCADE)
    fecha = models.CharField(max_length=6, default="000000")  # Almacena como texto en formato YYMMDD
    hora = models.CharField(max_length=4, default="0000")     # Almacena como texto en formato HHMM
    registros_validados = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    registros_preliminares = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    registros_no_validados = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Sensor {self.sensor.nombre_sensor} - Partícula {self.particula.nombre_particula}"


