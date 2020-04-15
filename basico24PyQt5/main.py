from PyQt5 import QtWidgets, uic
import sys


def boton_pulsado():
    print("BOTON PULSADO")
    win.etiqueta_ventana.setText("GRACIAS POR PULSAR EL BOTON")
    

#En PyQt5 es obligatorio tener el siguiente objeto
app = QtWidgets.QApplication([])

#win es el interfaz creado a partir de el siguiente archivo de diseño
win = uic.loadUi("ventana_ejemplo.ui")

#de esta forma se va a ejecutar la funcion boton_pulsado cuando se pulse en el boton_pulsame
win.boton_pulsame.clicked.connect(boton_pulsado)

#muestra la ventana
win.show()

#la aplicacion no cierra hasta que no termine app
sys.exit(app.exec_())