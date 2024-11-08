
from .models import SensorParticula
from django.shortcuts import get_object_or_404

class SensorParticulaDAO:
    
    @staticmethod
    def obtener_registro_por_particula_y_fecha(particula_id, fecha):
        """
        Recupera el registro de `SensorParticula` con el particula_id y la fecha especificados.
        """
        return SensorParticula.objects.filter(particula_id=particula_id, fecha=fecha).first()
