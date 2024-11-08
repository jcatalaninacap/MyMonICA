
from App.DAOSensorParticula import SensorParticulaDAO
from App.DTOSensorParticula import SensorParticulaDTO 
from django.core.exceptions import ObjectDoesNotExist


class SensorParticulaService:
    class SensorParticulaNoEncontrada(Exception):
        pass

    @staticmethod
    def obtener_estado_aire(particula_id, fecha):
        # Obtén el registro utilizando el DAO
        sensor_particula = SensorParticulaDAO.obtener_registro_por_particula_y_fecha(particula_id, fecha)
        
        if sensor_particula is None:
            # Si no se encuentra el registro, lanza una excepción personalizada
            raise SensorParticulaService.SensorParticulaNoEncontrada(
                "No hay datos para esta partícula en la fecha especificada"
            )
        
        registros_validados = sensor_particula.registros_validados

        # Determina el estado del aire según los umbrales
        if registros_validados < 50:
            return 'verde'
        elif 50 <= registros_validados <= 100:
            return 'amarillo'
        elif 100 < registros_validados <= 200:
            return 'naranja'
        elif registros_validados > 200:
            return 'rojo'
        return 'gris'  # Valor predeterminado para estado desconocido
