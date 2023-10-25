from src.domain.TragoBuilder import TragoBuilder

builder = TragoBuilder()    

trago1 = builder.set_nombre("Agua") \
                  .set_precio(500) \
                  .set_contenidoAlcohol(0) \
                  .build()
trago2 = builder.set_nombre("Sprite") \
                  .set_precio(800) \
                  .set_contenidoAlcohol(0) \
                  .build()
trago3 = builder.set_nombre("Whisky") \
                  .set_precio(2800) \
                  .set_contenidoAlcohol(80) \
                  .build()