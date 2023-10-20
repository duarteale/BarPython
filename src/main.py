from src.domain.bar import Bar
from src.controller.bartender import Bartender
from src.domain.jrBartender import JuniorBartender
from src.domain.srBartender import SeniorBartender
from src.view.view import BarView, BarController

if __name__ == "__main__":
      bar = Bar()
      view = BarView()
      controller = BarController(bar, view)

      '''builder = TragoBuilder()    
      trago = builder.set_nombre("Agua") \
                        .set_precio(500) \
                        .set_contenidoAlcohol(0) \
                        .build()'''

      # Chain
      junior_bartender = JuniorBartender("Juan Perez")
      senior_bartender = SeniorBartender("Andrés Lopez")
      junior_bartender.set_next(senior_bartender)
      bar.agregarBartender(junior_bartender)
      bar.agregarBartender(senior_bartender)

      menu = [{"nombre": "Sprite", "type": "Bebida sin alcohol", "precio": 800},
            {"nombre": "Whisky", "type": "Bebida con alcohol", "precio": 1800},
            {"nombre": "Jugo", "type": "Bebida sin alcohol", "precio": 450}]

      view.show_menu(menu)

      pedidos = [{"nombre": "Sprite", "type": "Bebida sin alcohol"},
                  {"nombre": "Jugo", "type": "Bebida sin alcohol"},
                  {"nombre": "Whisky", "type": "Bebida con alcohol"}]

      for pedido in pedidos:
            controller.tomarPedido(pedido)

      # Singleton para corroborar que realmente se aplique
      bar2 = Bar()
      print("Bar es igual a bar2?", bar is bar2)