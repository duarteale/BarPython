
from domain.Bebida import Bebida, Trago

class BebidaBuilder:
      def set_nombre(self, nombre):
            self.nombre = nombre
            return self

      def set_precio(self, precio):
            self.precio = precio
            return self

      def build(self):
            return Bebida(self.nombre, self.precio)

class TragoBuilder(BebidaBuilder):
      def set_contenidoAlcohol(self, contenidoAlcohol):
            self.contenidoAlcohol = contenidoAlcohol
            return self

      def build(self):
            return Trago(self.nombre, self.precio, self.contenidoAlcohol)