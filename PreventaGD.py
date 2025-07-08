import streamlit as st
import pandas as pd

# URL directa al archivo .xlsx
url = "https://growdatasas.sharepoint.com/:x:/s/Gestiondocumental/unidades_negocio/UN_Preventa/EarqLrDZ8SBAquq10_0MkjgBGjj2-ZcYeHg9_zCUmHtckQ?email=diana.urbano%40growdata.com.co&e=20wgCX&wdOrigin=TEAMS-MAGLEV.p2p_ns.rwc&wdExp=TEAMS-TREATMENT&wdhostclicktime=1751988159268&web=1"

# Leer el archivo
df = pd.read_excel(url)

# Mostrar en Streamlit
st.write("Tabla desde Excel en línea:")
st.dataframe(df)
