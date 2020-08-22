# Lista de especies para restauración

Este repositorio contiene:
- Un archivo Excel con nombres de especies de plantas.
- Un programa en Python para generar un archivo HTML a partir del archivo Excel y agregarle una columna con un enlace a una búsqueda en Google de las imágenes de cada especie.

El archivo generado puede visualizarse en []().

El programa se ejecuta en un ambiente Conda. A continuación, se detallan los pasos para ejecutar el programa

```shell
$ git clone 
```

## Creación y configuración del ambiente
```shell
# Actualización de Conda
$ conda update -n base -c defaults conda

# Creación del ambiente
$ conda create -n lista_especies_restauracion python=3

# Activación del ambiente
$ conda activate lista_especies_restauracion

# Instalación de paquetes
$ conda install -c anaconda xlrd

# Desactivación (para el final del proceso)
$ conda deactivate
```
