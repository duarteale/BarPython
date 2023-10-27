class Bar:
      _instance = None

      def __new__(cls):
            if cls._instance is None:
                  cls._instance = super(Bar, cls).__new__(cls)
                  cls._instance.bartenders = []
            return cls._instance      
      
      def agregarBartender(self, bartender):
            self.bartenders.append(bartender)
