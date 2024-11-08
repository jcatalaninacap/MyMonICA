
from django.shortcuts import render
from datetime import datetime
from App import DAOComunaImplement
from App.DAOSensorParticulaImplement import SensorParticulaService


def IndexView(request):
    '''Esta es la página principal'''
    return render(request, "index.html")


def mostrar_niveles(request):
    comuna_id = request.GET.get('comuna_id')
        # Convertir comuna_id a entero
    comuna_id = int(comuna_id)
    comuna = DAOComunaImplement.ComunaServiceDAO.obtener_comuna(comuna_id)
    
    fecha = request.GET.get('fecha')
    if fecha:
        try:
            # Convertir fecha a `datetime` y luego formatear a `yymmdd`
            fecha = datetime.strptime(fecha, "%Y-%m-%d").strftime("%y%m%d")
        except ValueError:
            # Manejo en caso de que el formato de la fecha no sea válido
            return render(request, 'error.html', {'mensaje': 'Fecha no válida.'})
    else:
        # Usa la fecha actual si no se proporciona en los parámetros
        fecha = datetime.now().strftime("%y%m%d")
        
    
    print(fecha,comuna_id)
    
    particulas = {}
    particulas_ids = {
        'NO2': 4,  # Puedes añadir más partículas aquí
    }
    
    for nombre, particula_id in particulas_ids.items():
        try:
            estado_aire = SensorParticulaService.obtener_estado_aire(particula_id, fecha)
            particulas[nombre] = estado_aire
        except SensorParticulaService.SensorParticulaNoEncontrada:
            particulas[nombre] = 'No hay datos'

    return render(request, 'semaforos.html', {'comuna': comuna, 'air_quality_data': particulas})