# Dev_Info_Exogena
Desarrollo de aplicativo para obtener informe general de ventas por cada cliente, de compras por cada proveedor y de la misma manera para devoluciones en ventas y compras.

## App Project

Para ejecutar el aplicativo es necesario seguir los siguientes pasos en la consola:

```sh
git clone
cd app
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt 
python3 main.py
```

### Ejemplos Insumos
Los ejemplos de los archivos con la información a procesar estan ubicados dentro del directorio Insumos, el formato de estos archivos es .xlsx

- Contactos_Clientes.xlsx
- Contactos_Proveedores.xlsx  
- Reporte_Impuestos_5-IVA.xlsx
- Reporte_Impuestos_19-IVA.xlsx
- Reporte_Impuestos_Exentos.xlsx

### Ejemplos Reportes
Los ejemplos de los archivos con la información a procesada y resultante del cruce de información estan ubicados dentro del directorio reportes, el formato de salida de estos archivos es .xlsx

- Compras.xlsx
- Devolucion_Copmras.xlsx
- Devolcuion_Ventas.xlsx
- Ventas.xlsx
- Ventas_Notas_Debitos.xlsx