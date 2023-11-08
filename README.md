
# Bar de bebidas

Este proyecto de Python simula un bar que utiliza los patrones de diseño Model-View-Controller (MVC), Chain of Responsibility, Singleton y Builder para gestionar la preparación de tragos. El bar cuenta con bartenders que determinan quién prepara cada bebida, ya sea un Junior (Jr.) o un Senior (Sr.), en función de si las bebidas contienen alcohol o no.- Bar del Proyecto
Este proyecto de Python simula un bar que utiliza los patrones de diseño Model-View-Controller (MVC), Chain of Responsibility, Singleton y Builder para gestionar la preparación de tragos. El bar cuenta con bartenders que determinan quién prepara cada bebida, ya sea un Junior (Jr.) o un Senior (Sr.), en función de si las bebidas contienen alcohol o no.


## Requisitos
  Asegúrate de tener Python 3.x instalado en tu sistema.


1- Clona el repositorio:
git clone https://github.com/duarteale/BarPython.git
cd BarPython


2- Crea un entorno virtual (opcional pero recomendado):
python -m venv venv
source venv/bin/activate

3- Instala las dependencias:
pip install -r requirements.txt
https://github.com/duarteale/BarPython.git


## Uso
  Ejecuta el programa principal desde main.py:
  python main.py

## Patrones de Diseño
  Este proyecto utiliza los siguientes patrones de diseño:

Model-View-Controller (MVC): Se utiliza para separar la lógica de la aplicación en tres componentes: Modelo, Vista y Controlador, lo que facilita la organización del código y la gestión de la interfaz de usuario.

Chain of Responsibility: Se utiliza para establecer una cadena de objetos que pueden procesar solicitudes en secuencia. En este proyecto, se aplica para que los bartenders junior y senior manejen las bebidas según su contenido de alcohol.

Singleton: Se utiliza para garantizar que solo haya una instancia de la clase BartenderManager, que gestiona la asignación de bartenders.

Builder: Se utiliza para construir objetos de bebida de manera flexible y parametrizable.


¡Disfruta de tu bar virtual con Python!
## Autor

- [@duarteale](https://www.github.com/duarteale)



## Agradecimientos

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

