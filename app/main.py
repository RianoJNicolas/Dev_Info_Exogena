import pandas as pd
import utils

def run():
    # Armado de Paths
    clientes = "Insumos/Contactos_Clientes.xlsx"
    proveedores = "Insumos/Contactos_Proveedores.xlsx"
    iva_0 = "Insumos/Reporte_Impuestos_Exentos.xlsx"
    iva_5 = "Insumos/Reporte_Impuestos_5-IVA.xlsx"
    iva_19 = "Insumos/Reporte_Impuestos_19-IVA.xlsx"

    # Obtencion de dataframes
    df_clientes = pd.read_excel(clientes)
    df_proveedores = pd.read_excel(proveedores)
    df_iva_0 = pd.read_excel(iva_0)
    df_iva_5 = pd.read_excel(iva_5)
    df_iva_19 = pd.read_excel(iva_19)
    print("Dfs obtenidos correctamente")

    # Obtener ventas, compras, devoluciones compras y devoluciones ventas

    # Ventas
    df_ventas = utils.get_forms(df_iva_0,df_iva_5,df_iva_19,df_clientes,"Factura")
    # Compras
    df_compras = utils.get_forms(df_iva_0,df_iva_5,df_iva_19,df_proveedores,"Factura de compra")
    # Notas debito / Devolucion en compras
    df_ND = utils.get_forms(df_iva_0,df_iva_5,df_iva_19,df_proveedores,"Nota débito")
    # Notas credito / Devolucion en ventas
    df_NC = utils.get_forms(df_iva_0,df_iva_5,df_iva_19,df_proveedores,"Nota crédito")
    
    # Guardado o generacion de archivos en excel
    df_compras.to_excel('InformeExogena_2022/Compras.xlsx', index=False)
    df_ND.to_excel('InformeExogena_2022/Devolucion_Compras.xlsx', index=False)
    df_ventas.to_excel('InformeExogena_2022/Ventas.xlsx', index=False)
    df_NC.to_excel('InformeExogena_2022/Devolucion_Ventas.xlsx', index=False)


if __name__ == '__main__':
  run()