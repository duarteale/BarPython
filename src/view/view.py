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

class BarController:
      def __init__(self, bar, view):
            self.bar = bar
            self.view = view

      def tomarPedido(self, pedido):
            nombreTrago = self.view.solicitar_nombreTrago()  
            pedido = {"nombre": nombreTrago}  
            trago = self.bar.hacerTrago(pedido)
            if trago:
                  self.view.pedidoAceptado(trago.nombre, trago.preparado_por.nombreBartender)
            else:
                  print("No puedo servirle esa bebida, no tengo stock.")

controller = BarController(bar)   