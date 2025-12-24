#imports
import sys
from mysql.connector import Error

'''
#imports de los DAO
from dao.db import Connection
from dao.ruta_dao import RutaDAO
from dao.corrida_dao import CorridaDAO
from dao.reservacion_dao import ReservacionDAO

#imports de los Servicios
from servicios.servicios_de_consulta import ServiciosDeConsulta

#imports de los Controladores
from controladores.controlador_ruta import ControladorRuta
from controladores.controlador_ventana_horarios import ControladorVentanaHorarios
from controladores.controlador_ve_reservaciones import ControladorVEReservaciones

#imports de la interfaz grafica
#from ui.main_ui import MainUI
from PySide6.QtWidgets import QApplication
from ui.ve_ventana_reservaciones import VentanaReservaciones as MainUI

#imports de utilidades
from utilidades.app_contenedor import AppContenedor

#imports para testeo
from objetos.ruta import Ruta
'''

#importing daos
from repositories.connection import Connection

#importing view
from view.main_view import MainView

def main():
    print('Iniciando Transportes Cuervo Negro')
    #Iniciando conexion
    try:

        Connection.getConnection()
        print('Conexion con la BD hecha.')

    except Error as e:
        print(f"ERROR IMPORTANTE: No se pudo iniciar el programa. {e}")
        Connection.closeConnection() #cerrando por si acaso algo quedo abierto en la conexion
        return #terminando la ejecucion del programa
    
    
    # iniciando vista
    vista_principal = MainView()
    vista_principal.run()

    #cerrando conexion
    if Connection.closeConnection():
        print('Cerrando conexion con la BD.')
    sys.exit(0)

'''
    #Iniciando dao's
    ruta_dao = RutaDAO()
    corrida_dao = CorridaDAO()
    reservacion_dao = ReservacionDAO()
    
    #Iniciando servicios
    servicios_de_consulta = ServiciosDeConsulta(ruta_dao,corrida_dao,reservacion_dao)

    #Iniciando controladores
    controlador_ruta = ControladorRuta(servicios_de_consulta)
    controlador_ventana_horarios = ControladorVentanaHorarios(servicios_de_consulta)
    controlador_ve_reservaciones = ControladorVEReservaciones(servicios_de_consulta)

    
    app_manager = AppContenedor(
                                ruta_controlador=controlador_ruta,
                                controlador_ventana_horarios=controlador_ventana_horarios,
                                controlador_ve_reservaciones=controlador_ve_reservaciones)

    #iniciando UI
    print('Iniciando UI')
    app = QApplication(sys.argv)
    ventana = MainUI(app_manager)
    ventana.show()
'''

if __name__ == '__main__':
    main()

