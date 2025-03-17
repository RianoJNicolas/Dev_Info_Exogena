import pandas as pd
import utils
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def run():
    logging.info("Iniciando el aplicativo")
    # Armado de Paths
    clientes = "Insumos/Contactos_Clientes.xlsx"
    proveedores = "Insumos/Contactos_Proveedores.xlsx"
    iva_0 = "Insumos/Reporte_Impuestos_Exentos.xlsx"
    iva_5 = "Insumos/Reporte_Impuestos_5-IVA.xlsx"
    iva_19 = "Insumos/Reporte_Impuestos_19-IVA.xlsx"
    
    # Obtencion de dataframes
    logging.info("Cargando Dfs de insumos")
    df_clientes = pd.read_excel(clientes)
    df_proveedores = pd.read_excel(proveedores)
    df_iva_0 = pd.read_excel(iva_0)
    df_iva_5 = pd.read_excel(iva_5)
    df_iva_19 = pd.read_excel(iva_19)
    logging.info("Dfs obtenidos correctamente")

    # Obtener ventas, compras, devoluciones compras y devoluciones ventas
    # Ventas
    logging.info("Iniciando procesamiento y cruce de datos")
    df_ventas = utils.get_forms(df_iva_0, df_iva_5, df_iva_19, df_clientes, "Factura de venta")
    # Notas debito de ingresos
    df_ventas_nd = utils.get_forms(df_iva_0, df_iva_5, df_iva_19, df_clientes, "Nota débito en ingresos")
    # Compras
    df_compras = utils.get_forms(df_iva_0, df_iva_5, df_iva_19, df_proveedores, "Factura de compra")
    # Notas debito / Devolucion en compras
    df_ND = utils.get_forms(df_iva_0, df_iva_5, df_iva_19, df_proveedores, "Nota débito")
    # Notas credito / Devolucion en ventas
    df_NC = utils.get_forms(df_iva_0, df_iva_5, df_iva_19, df_clientes, "Nota crédito")
    logging.info("Reportes obtenidos correctamente")

    # Guardado o generacion de archivos en excel
    logging.info("Iniciando escritura de Reportes")
    df_compras.to_excel('Reportes/Compras.xlsx', index=False)
    df_ND.to_excel('Reportes/Devolucion_Compras.xlsx', index=False)
    df_ventas.to_excel('Reportes/Ventas.xlsx', index=False)
    df_ventas_nd.to_excel('Reportes/Ventas_Notas_Debito.xlsx', index=False)
    df_NC.to_excel('Reportes/Devolucion_Ventas.xlsx', index=False)
    logging.info("Finalizacion de escritura de Reportes correctamente")


if __name__ == '__main__':
  run()