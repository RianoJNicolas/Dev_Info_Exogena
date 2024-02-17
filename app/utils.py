import pandas as pd

def get_dfs(df_0,df_5,df_19,key_field):
    """
        inputs:
        df_0  -> Dataframe correspondiente a datos con IVA cero/excentos
        df_5  -> Dataframe correspondiente a datos con IVA 5%
        df_19 -> Dataframe correspondiente a datos con IVA 19%
        key_field -> String que puede tomar cuatro valores (Factura, Factura de compra,Nota débito,Nota crédito)
        outputs:
        df_result -> Dataframe con datos con IVA 0, 5 y 19
    """
    
    # Obtencion de datframes de ventas, compras, notas credito o notas debito
    df_0 = df_0.loc[df_0['Tipo de documento'] == key_field]
    df_5 = df_5.loc[df_5['Tipo de documento'] == key_field]
    df_19 = df_19.loc[df_19['Tipo de documento'] == key_field]

    # Actualizacion de nombres de las columnas y eliminando columnas
    if (key_field == "Factura"):
        # Actualizacion de nombres
        df_0 = df_0.rename(columns={"Base ventas": "Excento"})

        df_5 = df_5.rename(columns={"Base ventas": "Base IVA-5%"})
        df_5 = df_5.rename(columns={"Impuesto en ventas": "IVA-5%"})

        df_19 = df_19.rename(columns={"Base ventas": "Base IVA-19%"})
        df_19 = df_19.rename(columns={"Impuesto en ventas": "IVA-19%"})

        # Eliminando columnas no necesarias
        df_0 = df_0.drop(['Base compras','Impuesto en compras','Base devolución ventas',
                        'Impuesto devolución ventas','Base devolución compras',
                        'Impuesto devolución compras'], axis=1)
        df_5 = df_5.drop(['Base compras','Impuesto en compras','Base devolución ventas',
                        'Impuesto devolución ventas','Base devolución compras',
                        'Impuesto devolución compras'], axis=1)
        df_19 = df_19.drop(['Base compras','Impuesto en compras','Base devolución ventas',
                        'Impuesto devolución ventas','Base devolución compras',
                        'Impuesto devolución compras'], axis=1)
        
    elif (key_field == "Factura de compra"):
        # Actualizacion de nombres
        df_0 = df_0.rename(columns={"Base compras": "Excento"})

        df_5 = df_5.rename(columns={"Base compras": "Base IVA-5%"})
        df_5 = df_5.rename(columns={"Impuesto en compras": "IVA-5%"})

        df_19 = df_19.rename(columns={"Base compras": "Base IVA-19%"})
        df_19 = df_19.rename(columns={"Impuesto en compras": "IVA-19%"})

        # Eliminando columnas no necesarias
        df_0 = df_0.drop(['Base ventas','Impuesto en ventas','Base devolución ventas',
                        'Impuesto devolución ventas','Base devolución compras',
                        'Impuesto devolución compras'], axis=1)
        df_5 = df_5.drop(['Base ventas','Impuesto en ventas','Base devolución ventas',
                        'Impuesto devolución ventas','Base devolución compras',
                        'Impuesto devolución compras'], axis=1)
        df_19 = df_19.drop(['Base ventas','Impuesto en ventas','Base devolución ventas',
                        'Impuesto devolución ventas','Base devolución compras',
                        'Impuesto devolución compras'], axis=1)
        
    elif (key_field == "Nota débito"):
        # Actualizacion de nombres
        df_0 = df_0.rename(columns={"Base devolución compras": "Excento"})

        df_5 = df_5.rename(columns={"Base devolución compras": "Base IVA-5%"})
        df_5 = df_5.rename(columns={"Impuesto devolución compras": "IVA-5%"})

        df_19 = df_19.rename(columns={"Base devolución compras": "Base IVA-19%"})
        df_19 = df_19.rename(columns={"Impuesto devolución compras": "IVA-19%"})

        # Eliminando columnas no necesarias
        df_0 = df_0.drop(['Base ventas','Impuesto en ventas','Base devolución ventas',
                        'Impuesto devolución ventas','Base compras','Impuesto en compras'], axis=1)
        df_5 = df_5.drop(['Base ventas','Impuesto en ventas','Base devolución ventas',
                        'Impuesto devolución ventas','Base compras','Impuesto en compras'], axis=1)
        df_19 = df_19.drop(['Base ventas','Impuesto en ventas','Base devolución ventas',
                        'Impuesto devolución ventas','Base compras','Impuesto en compras'], axis=1)

    elif (key_field == "Nota crédito"):
        df_0 = df_0.rename(columns={"Base devolución ventas": "Excento"})

        df_5 = df_5.rename(columns={"Base devolución ventas": "Base IVA-5%"})
        df_5 = df_5.rename(columns={"Impuesto devolución ventas": "IVA-5%"})

        df_19 = df_19.rename(columns={"Base devolución ventas": "Base IVA-19%"})
        df_19 = df_19.rename(columns={"Impuesto devolución ventas": "IVA-19%"})

        # Eliminando columnas no necesarias
        df_0 = df_0.drop(['Base ventas','Impuesto en ventas','Base compras',
                        'Impuesto en compras','Base devolución compras',
                        'Impuesto devolución compras'], axis=1)
        df_5 = df_5.drop(['Base ventas','Impuesto en ventas','Base compras',
                        'Impuesto en compras','Base devolución compras',
                        'Impuesto devolución compras'], axis=1)
        df_19 = df_19.drop(['Base ventas','Impuesto en ventas','Base compras',
                        'Impuesto en compras','Base devolución compras',
                        'Impuesto devolución compras'], axis=1) 
    
    # Union o merge de dataframes
    df_1 = pd.merge(df_5, df_0, on='Comprobante', how="outer")
    df_result = pd.merge(df_19, df_1, on='Comprobante', how="outer")

    # Eliminando datos en Nan
    df_result['Identificación'] = df_result['Identificación'].fillna(df_result['Identificación_x'])
    df_result['Nombre del tercero'] = df_result['Nombre del tercero'].fillna(df_result['Nombre del tercero_x'])
    
    df_result['Identificación'] = df_result['Identificación'].fillna(df_result['Identificación_y'])
    df_result['Nombre del tercero'] = df_result['Nombre del tercero'].fillna(df_result['Nombre del tercero_y'])

    df_result = df_result[['Comprobante','Nombre del tercero','Identificación','Base IVA-19%','IVA-19%','Base IVA-5%','IVA-5%','Excento']]

    # Sumando valores por cada Nombre del tercero e identificacion
    df_sum = df_result.groupby(['Identificación','Nombre del tercero'])[['Base IVA-19%', 'IVA-19%','Base IVA-5%','IVA-5%','Excento']].sum()
    df_sum = df_sum.reset_index()
    df_sum = df_sum.rename(columns={'Identificación': 'Identificación', 'Nombre del tercero': 'Nombre del tercero'})
    df_sum['Identificación'] = df_sum['Identificación'].astype(int).astype(str)
    df_sum['Nombre del tercero'] = df_sum['Nombre del tercero'].str.upper()
    return df_result, df_sum


# Funcion para agregar datos personales
def fit_dates(df_contactos,df,tipo_documento):
    """
    Inputs:
        df_contactos -> Dataframe con los datos de clientes o proveedores
        df -> Dataframe con los datos de ventas, compras o devoluciones
        tipo_documento (string) -> Especifica el tipo de documento a obtener
    Outputs_
        df_result -> Dataframe con los datos + contactos
    """
    df_result = df
    if (tipo_documento == "Factura") or (tipo_documento == "Nota crédito"):
        # Preparacion de df y df_contactos para clientes
        df_contactos['Nombre'] = df_contactos['Nombre'].fillna(value='').str.strip()
        df_contactos['Segundo nombre'] = df_contactos['Segundo nombre'].fillna(value='').str.strip()
        df_contactos['Primer apellido'] = df_contactos['Primer apellido'].fillna(value='').str.strip()
        df_contactos['Segundo apellido'] = df_contactos['Segundo apellido'].fillna(value='').str.strip()
        df_contactos["Cliente"] = df_contactos.apply(lambda x: "{} {} {} {}".format(x["Nombre"], x["Segundo nombre"], x["Primer apellido"], x["Segundo apellido"]), axis=1)
        df_contactos["Cliente"] = df_contactos["Cliente"].str.upper()
        df_contactos["Direccion"] = df_contactos.apply(lambda x: "{}, {} ".format(x["Dirección"], x["Municipio"]), axis=1)
        df_contactos["Direccion"] = df_contactos["Direccion"].str.upper()
        df_contactos['Identificación'] = df_contactos['Identificación'].astype(str)  
        df_contactos = df_contactos.rename(columns={'Teléfono 1': 'Tel / Celular'})   
        df_contactos = df_contactos[['Cliente','Identificación','Dígito de verificación','Direccion','Tel / Celular','Correo']]
        df_contactos = df_contactos.drop_duplicates(['Identificación'])
        
        df = df.rename(columns={'Nombre del tercero': 'Cliente'})
        # Agregando datos de contacto al dataframe df
        df_result = pd.merge(df, df_contactos, on='Identificación', how="left")
        df_result = df_result.rename(columns={'Cliente_x': 'Cliente'}) 
        df_result = df_result[['Cliente','Identificación','Dígito de verificación','Direccion','Tel / Celular','Correo','Base IVA-19%', 'IVA-19%','Base IVA-5%','IVA-5%','Excento']]

    elif (tipo_documento == "Factura de compra") or (tipo_documento == "Nota débito"):
        # Preparacion de df y df_contactos para proveedores
        df_contactos['Dígito de verificación'] = df_contactos['Dígito de verificación'].fillna(value='0')
        df_contactos['Dígito de verificación'] = df_contactos['Dígito de verificación'].astype(float).astype(int).astype(str)
        df_contactos['Nombre'] = df_contactos['Nombre'].fillna(value='').str.strip()
        df_contactos['Segundo nombre'] = df_contactos['Segundo nombre'].fillna(value='').str.strip()
        df_contactos['Primer apellido'] = df_contactos['Primer apellido'].fillna(value='').str.strip()
        df_contactos['Segundo apellido'] = df_contactos['Segundo apellido'].fillna(value='').str.strip()
        df_contactos["Proveedor"] = df_contactos.apply(lambda x: "{} {} {} {}".format(x["Nombre"], x["Segundo nombre"], x["Primer apellido"], x["Segundo apellido"]), axis=1)
        df_contactos["Proveedor"] = df_contactos["Proveedor"].str.upper()
        df_contactos["Direccion"] = df_contactos.apply(lambda x: "{}, {} ".format(x["Dirección"], x["Municipio"]), axis=1)
        df_contactos["Direccion"] = df_contactos["Direccion"].str.upper()
        df_contactos['Identificación'] = df_contactos['Identificación'].astype(str)  
        df_contactos = df_contactos.rename(columns={'Teléfono 1': 'Tel / Celular'})   
        df_contactos = df_contactos[['Proveedor','Identificación','Dígito de verificación','Direccion','Tel / Celular','Correo']]
        
        df = df.rename(columns={'Nombre del tercero': 'Proveedor'})
        # Agregando datos de contacto al dataframe df
        df_result = pd.merge(df, df_contactos, on='Identificación', how="left")
        df_result = df_result.rename(columns={'Proveedor_x': 'Proveedor'}) 
        df_result = df_result[['Proveedor','Identificación','Dígito de verificación','Direccion','Tel / Celular','Correo','Base IVA-19%', 'IVA-19%','Base IVA-5%','IVA-5%','Excento']]
    return df_result


def get_forms(df_0,df_5,df_19,df_contactos,tipo_documento):
    df1 = get_dfs(df_0,df_5,df_19,tipo_documento)
    df_f = fit_dates(df_contactos,df1[1],tipo_documento)
    return df_f