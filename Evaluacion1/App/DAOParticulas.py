from django.shortcuts import get_object_or_404
from App.models import Particula
from App import DTOParticulas

class ParticulasDAO:
    @staticmethod
    def obtener_todas_las_particulas():
        particulas = Particula.objects.all()
        return [DTOParticulas.ParticulaDTO(particula.id_particula,particula.nombre_particula,particula.descripcion) for particula in particulas]
    
    
    @staticmethod
    def obtener_particula_por_id(id_particula):
        particula = get_object_or_404(Particula, id_particula=id_particula)
        return DTOParticulas.ParticulaDTO(particula.id_particula,particula.nombre_particula,particula.descripcion)