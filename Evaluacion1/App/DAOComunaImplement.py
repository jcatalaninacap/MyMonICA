
from App import DAOComuna

class ComunaServiceDAO:
    
    @staticmethod
    def listar_comunas():
        return DAOComuna.ComunaDAO.obtener_todas_las_comunas()

    @staticmethod
    def obtener_comuna(id_comuna):
        return DAOComuna.ComunaDAO.obtener_comuna_por_id(id_comuna) if id_comuna != 'todas' else None
