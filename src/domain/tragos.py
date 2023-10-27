from src.domain.bebida import Bebida

class Trago(Bebida):
      def __init__(self, nombre, precio, contenidoAlcohol):
            super().__init__(nombre, precio)
            self.contenidoAlcohol = contenidoAlcohol

      def preparar(self):
            pass