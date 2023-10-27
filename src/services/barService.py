from domain.bar import Bar

bar = Bar()
# Singleton para corroborar que realmente se aplique
bar2 = Bar()
print("Bar es igual a bar2?", bar is bar2)