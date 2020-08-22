# Lista de especies para restauración

Este repositorio contiene:
- Un archivo Excel con nombre de especies de plantas.
- Un programa en Python para generar un archivo HTML a partir del archivo Excel y agregar una columna con un enlace a una búsqueda en Google de las imágenes de las especies.

## Creación y mantenimiento de un ambiente Conda
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


<table>
  <tr><th>Familia</th><th>Nombre científico</th><th>Imágenes en Google</th></tr>
  <tr><td>Anacardiaceae</td><td>Anacardium excelsum</td><td> <a href="https://www.google.com/search?tbm=isch&q=Anacardium+excelsum">Anacardium excelsum - Google</a></td></tr>
  <tr><td>Anacardiaceae</td><td>Anacardium occidentale</td><td> <a href="https://www.google.com/search?tbm=isch&q=Anacardium+occidentale">Anacardium occidentale - Google</a></td></tr>
    <tr><td>Anacardiaceae</td><td>Astronium graveolens</td><td> <a href="https://www.google.com/search?tbm=isch&q=Astronium graveolens">Astronium graveolens - Google</a></td></tr>
</table>
