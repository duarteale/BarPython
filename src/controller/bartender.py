from domain.jrBartender import JuniorBartender
from domain.srBartender import SeniorBartender
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

      junior_bartender = JuniorBartender("Juan Perez")
      senior_bartender = SeniorBartender("Andrés Lopez")
      junior_bartender.set_next(senior_bartender)
      bar.agregarBartender(junior_bartender)
      bar.agregarBartender(senior_bartender)