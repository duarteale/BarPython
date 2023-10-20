from src.domain.bebida import Bebida


class Bartender:
      def __init__(self, nombre):
            self.nombre = nombre
            self.next_bartender = None

      def set_next(self, next_bartender):
            self.next_bartender = next_bartender
            return next_bartender

      def prepararTrago(self, pedido):
            if "type" in pedido and self.servir(pedido):
                  trago = self.hacerTrago(pedido)
                  if trago:
                        return trago
            if self.next_bartender:
                  return self.next_bartender.prepararTrago(pedido)
            return None

      def servir(self, pedido):
            pass

      def hacerTrago(self, pedido):
            pass
