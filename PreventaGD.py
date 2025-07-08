import streamlit as st
import pandas as pd
import urllib

# URL directa al archivo .xlsx
url = "https://growdatasas.sharepoint.com/:x:/s/Gestiondocumental/unidades_negocio/UN_Preventa/EarqLrDZ8SBAquq10_0MkjgBGjj2-ZcYeHg9_zCUmHtckQ?email=diana.urbano%40growdata.com.co&e=20wgCX&wdOrigin=TEAMS-MAGLEV.p2p_ns.rwc&wdExp=TEAMS-TREATMENT&wdhostclicktime=1751988159268&web=1"

# Leer el archivo
#df = pd.read_excel(url)

# Mostrar en Streamlit
#st.write("Tabla desde Excel en línea:")
#st.dataframe(df)

# Nombre real del archivo (ajusta esto)
archivo_nombre = "tareas semana del 24 al 27 de junio .xlsx"

# Ruta completa al archivo dentro de SharePoint (ajústala según tu estructura real)
ruta_relativa = "/sites/Gestiondocumental/unidades_negocio/UN_Preventa/" + archivo_nombre

# Codificamos la ruta
source_url = urllib.parse.quote(ruta_relativa)

# Construimos la URL de descarga directa
url_descarga = f"https://growdatasas.sharepoint.com/_layouts/15/download.aspx?SourceUrl={source_url}"

# Leemos el archivo Excel directamente desde SharePoint
df = pd.read_excel(url_descarga)

# Mostramos en Streamlit
st.title("Datos desde SharePoint")
st.dataframe(df)
