import sys
from classes.Interface import Interface


class Menu:

    def __init__(self):
        self.showMenu()

    @staticmethod
    def endProg():
        print("\n")
        print("Fin del programa")
        sys.exit()

    def showMenu(self):
        print(
            "\n\nMENU\n"
            "\n1) Mostrar Temperatura y humedad"
            "\n2) Mostrar Presencia"
            "\n3) Mostrar Distancia"
            "\n4) Salir")
        opc = input("\nSeleccione una opcion: ")
        if int(opc) < 5:
            if int(opc) > 0:
                while opc != "4":
                    if opc == "1":
                        Interface.showDHT()
                        self.showMenu()
                    elif opc == "2":
                        Interface.showHCS()
                        self.showMenu()
                    elif opc == "3":
                        Interface.showPIR()
                        self.showMenu()
                else:
                    self.endProg()
            else:
                print("\nOpcion no valida")
                self.showMenu()
        else:
            print("\nOpcion no valida")
            self.showMenu()
