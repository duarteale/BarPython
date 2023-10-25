class BarController:
      def __init__(self, bar, view):
            self.bar = bar
            self.view = view

      def tomarPedido(self, pedido):
            nombreTrago = self.view.solicitar_nombreTrago()  
            pedido = {"nombre": nombreTrago}  
            trago = self.bar.hacerTrago(pedido)
            if trago:
                  self.view.pedidoAceptado(trago.nombre, trago.preparado_por.nombreBartender)
            else:
                  print("No puedo servirle esa bebida, no tengo stock.")