

from django.shortcuts import get_object_or_404
from App.models import Comuna
from App import DTOComuna

class ComunaDAO:
    @staticmethod
    def obtener_todas_las_comunas():
        comunas = Comuna.objects.all()
        return [DTOComuna.ComunaDTO(comuna.id_comuna, comuna.nombre_comuna) for comuna in comunas]

    @staticmethod
    def obtener_comuna_por_id(id_comuna):
        comuna = get_object_or_404(Comuna, id_comuna=id_comuna)
        return DTOComuna.ComunaDTO(comuna.id_comuna, comuna.nombre_comuna)
