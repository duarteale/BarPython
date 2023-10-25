
from domain.bebida import Bebida, Trago

class TragoBuilder:
      def __init__(self):
            self.nombre = ""
            self.precio = 0
            self.contenidoAlcohol = 0

      def set_nombre(self, nombre):
            self.nombre = nombre
            return self

      def set_precio(self, precio):
            self.precio = precio
            return self

      def set_contenidoAlcohol(self, contenidoAlcohol):
            self.contenidoAlcohol = contenidoAlcohol
            return self

      def build(self):
            return Trago(self.nombre, self.precio, self.contenidoAlcohol)