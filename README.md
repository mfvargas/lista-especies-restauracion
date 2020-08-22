# Lista de especies para restauración

Este repositorio contiene:
- Un archivo Excel con nombres de especies de plantas.
- Un programa en Python para generar un archivo HTML a partir del archivo Excel y agregarle una columna con un enlace a una búsqueda en Google de las imágenes de cada especie.

El archivo generado puede visualizarse en [https://mfvargas.github.io/lista-especies-restauracion/](https://mfvargas.github.io/lista-especies-restauracion/).

El programa se ejecuta en un ambiente Conda. A continuación, se detallan los pasos para ejecutar el programa.

**Ejecución normal del programa**
```shell
# Clonación del repositorio
$ git clone https://github.com/mfvargas/lista-especies-restauracion.git
$ cd lista-especies-restauracion

# Activación del ambiente Conda
$ conda activate lista_especies_restauracion

# Ejecución del programa
$ python lista-especies-restauracion.py

# Actualización del repositorio y del archivo HTML generado
$ git add .
$ git commit -m "Generar nuevo archivo HTML"
$ git push

# Desactivación del ambiente Conda
$ conda deactivate
```

**Creación y configuración del ambiente Conda (solo de hacerse una vez)**
```shell
# Actualización de Conda
$ conda update -n base -c defaults conda

# Creación del ambiente
$ conda create -n lista_especies_restauracion python=3

# Activación del ambiente
$ conda activate lista_especies_restauracion

# Instalación de paquetes
$ conda install -c anaconda xlrd

# Desactivación del ambiente
$ conda deactivate
```
