# Este programa lee un archivo Excel con nombres de especies
# y retorna un archivo HTML con una columna adicional
# correspondiente a una búsqueda en Google de las imágenes de cada especie

import xlrd

INPUT_FILE_NAME = "lista-especies-restauracion.xlsx"
OUTPUT_FILE_NAME = "index.html"

URL_BASE = "https://www.google.com/search?tbm=isch&q"

wb = xlrd.open_workbook(INPUT_FILE_NAME)
sheet = wb.sheet_by_index(0) 

with open(OUTPUT_FILE_NAME, "w") as output_file:
    output_file.write('<!doctype html>')
    output_file.write('<html lang="es">')
    output_file.write('<head>')
    output_file.write('  <meta charset="utf-8">')
    output_file.write('  <title>Lista de especies para restauración</title>')
    output_file.write('</head>')
    output_file.write('<body>')
    output_file.write('<h1>Lista de especies para restauración</h1>')
    output_file.write('  <table>')
    output_file.write('    <tr><th>Familia</th><th>Nombre científico</th><th>Imágenes en Google</th></tr>')
    
    # Recorrido del archivo Excel
    for i in range(1, sheet.nrows):
        family = sheet.cell_value(i, 0)
        scientific_name = sheet.cell_value(i, 1)
        genus = scientific_name.split(' ')[0]
        specific_epithet = scientific_name.split(' ')[1]
        print(genus, specific_epithet)
    
        output_file.write(f'    <tr>')
        output_file.write(f'<td>{family}</td>')
        output_file.write(f'<td>{scientific_name}</td>')
        output_file.write(f'<td><a href="{URL_BASE}={genus}+{specific_epithet}">{scientific_name} - Google</a></td>')
        output_file.write(f'</tr>')
            
    output_file.write('  </table>')
    output_file.write('</body>')
    output_file.write('</html>') 