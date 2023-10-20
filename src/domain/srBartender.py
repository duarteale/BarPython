from src.domain.bebida import Bebida
from src.controller.bartender import Bartender

class SeniorBartender(Bartender):
      def servir(self, pedido):
            if "type" in pedido and pedido["type"] == "Bebida con alcohol":
                  return True
            return False

      def hacerTrago(self, pedido):
            return f"{pedido['nombre']} (Bebida con alcohol) by {self.nombre}"
