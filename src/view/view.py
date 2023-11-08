from controller.controller import BarController

class BarView:
      def solicitar_nombreTrago(self):
            nombreTrago = input("Ingrese el nombre del trago que desea preparar: ")
            return nombreTrago

      def show_menu(self, menu):
            print("Menu:")
            for item in menu:
                  print(f"{item['nombre']}: ${item['precio']}")

      def pedidoAceptado(self, nombreTrago, nombreBartender):
            print(f"Aquí tiene su trago: {nombreTrago}, preparado por {nombreBartender}, que lo disfrute!")

      menu = [{"nombre": "Sprite", "type": "Bebida sin alcohol", "precio": 800},
      {"nombre": "Whisky", "type": "Bebida con alcohol", "precio": 1800},
      {"nombre": "Jugo", "type": "Bebida sin alcohol", "precio": 450}]

controller = BarController(bar)   