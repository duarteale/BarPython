from src.domain.bebida import Bebida
from src.controller.bartender import Bartender

class JuniorBartender(Bartender):
      def servir(self, pedido):
            if "type" in pedido and pedido["type"] == "Bebida sin alcohol":
                  return True
            return False

      def hacerTrago(self, pedido):
            for bartender in self.bartenders:
                  trago = bartender.prepararTrago(pedido)
                  if trago:
                        return  f"{pedido['nombre']} (Bebida sin alcohol) by {self.nombre}"
            return None