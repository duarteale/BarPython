from abc import ABC, abstractmethod

class AbstractBartender(ABC):
      def __init__(self, nombre):
            self.nombre = nombre

      @abstractmethod
      def servir(self, pedido):
            pass

      @abstractmethod
      def hacerTrago(self, pedido):
            pass