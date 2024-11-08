
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

        estado, color = SensorParticulaService.determinar_estado_calidad_aire(registro, particula_id)
        
        #print(f"Estado: {estado}, Color: {color}")

        return color
    
    @staticmethod
    def determinar_estado_calidad_aire(valor, tipo_contaminante):

        #   tipo_contaminante:  'PM10', 'PM2.5', 'O3', 'NO2', 'CO' o 'SO2'.
        
        if tipo_contaminante == 1:
            if valor < 50:
                return 'Buena', 'verde'
            elif 50 <= valor <= 80:
                return 'Regular', 'amarillo'
            elif 80 < valor <= 110:
                return 'Alerta', 'naranja'
            elif 110 < valor <= 170:
                return 'Preemergencia', 'rojo'
            elif valor > 170:
                return 'Emergencia', 'rojo'


        elif tipo_contaminante == 2:
            if valor < 25:
                return 'Buena', 'verde'
            elif 25 <= valor <= 37:
                return 'Regular', 'amarillo'
            elif 37 < valor <= 55:
                return 'Alerta', 'naranja'
            elif 55 < valor <= 110:
                return 'Preemergencia', 'rojo'
            elif valor > 110:
                return 'Emergencia', 'rojo'


        elif tipo_contaminante == 3 :
            if valor < 100:
                return 'Buena', 'verde'
            elif 100 <= valor <= 160:
                return 'Regular', 'amarillo'
            elif 160 < valor <= 200:
                return 'Alerta', 'naranja'
            elif 200 < valor <= 300:
                return 'Preemergencia', 'rojo'
            elif valor > 300:
                return 'Emergencia', 'rojo'
    

        elif tipo_contaminante == 4 :
            if valor < 50:
                return 'Buena', 'verde'
            elif 50 <= valor <= 100:
                return 'Regular', 'amarillo'
            elif 100 < valor <= 200:
                return 'Alerta', 'naranja'
            elif valor > 200:
                return 'Emergencia', 'rojo'


        elif tipo_contaminante == 6:
            if valor < 9:
                return 'Buena', 'verde'
            elif 9 <= valor <= 15:
                return 'Regular', 'amarillo'
            elif 15 < valor <= 30:
                return 'Alerta', 'naranja'
            elif valor > 30:
                return 'Emergencia', 'rojo'


        elif tipo_contaminante == 5:
            if valor < 50:
                return 'Buena', 'verde'
            elif 50 <= valor <= 100:
                return 'Regular', 'amarillo'
            elif 100 < valor <= 250:
                return 'Alerta', 'naranja'
            elif valor > 250:
                return 'Emergencia', 'rojo'


        return 'Desconocido', 'gris'  # Valor predeterminado si el tipo de contaminante no es válido

        
        






