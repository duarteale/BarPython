class BartenderService:
      def set_next(self, next_bartender):
            self.next_bartender = next_bartender
            return next_bartender

      def prepararTrago(self, pedido):
            if self.servir(pedido):
                  return self.hacerTrago(pedido)
            if self.next_bartender:
                  return self.next_bartender.prepararTrago(pedido)
            return None