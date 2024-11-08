
from App.DAOSensorParticula import SensorParticulaDAO
from App.DTOSensorParticula import SensorParticulaDTO 
from django.core.exceptions import ObjectDoesNotExist


class SensorParticulaService:
    class SensorParticulaNoEncontrada(Exception):
        pass
    
    @staticmethod
    def verificar_registros(registros_validados,registros_preliminares,registros_no_validados):

        if registros_validados > 0:
            return registros_validados
        elif registros_preliminares > 0:
            return registros_preliminares
        elif registros_no_validados > 0:
            return registros_no_validados
        else:
            return registros_validados

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
        registros_preliminares = sensor_particula.registros_preliminares
        registros_no_validados = sensor_particula.registros_no_validados
        
        # Llamada correcta al método estático
        registro = SensorParticulaService.verificar_registros(
            registros_validados, registros_preliminares, registros_no_validados
        )




        # Determina el estado del aire según los umbrales
        # 4 - NO2 - Dióxido de Nitrógeno
        if registro < 50:
            return 'verde'
        elif 50 <= registro <= 100:
            return 'amarillo'
        elif 100 < registro <= 200:
            return 'naranja'
        elif registro > 200:
            return 'rojo'
        return 'gris'  # Valor predeterminado para estado desconocido
    
    


