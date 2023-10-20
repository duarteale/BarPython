class Bar:
      _instance = None

      def __new__(cls):
            if cls._instance is None:
                  cls._instance = super(Bar, cls).__new__(cls)
                  cls._instance.bartenders = []
            return cls._instance

      def hacerTrago(self, pedido):
            for bartender in self.bartenders:
                  trago = bartender.prepararTrago(pedido)
                  if trago:
                        return trago
            return None
      
      def agregarBartender(self, bartender):
            self.bartenders.append(bartender)
