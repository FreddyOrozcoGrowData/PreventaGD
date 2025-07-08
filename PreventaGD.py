#url = "https://growdatasas.sharepoint.com/:x:/s/Gestiondocumental/unidades_negocio/UN_Preventa/EarqLrDZ8SBAquq10_0MkjgBGjj2-ZcYeHg9_zCUmHtckQ?email=diana.urbano%40growdata.com.co&e=20wgCX&wdOrigin=TEAMS-MAGLEV.p2p_ns.rwc&wdExp=TEAMS-TREATMENT&wdhostclicktime=1751988159268&web=1"
import streamlit as st
import pandas as pd
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from io import BytesIO

# CONFIGURA ESTOS DATOS
sharepoint_url = "https://growdatasas.sharepoint.com"
site_url = "/sites/Gestiondocumental"
folder_path = "/unidades_negocio/UN_Preventa"
file_name = "tareas semana del 24 al 27 de junio .xlsx"  # ← cambia por el nombre exacto de tu archivo

username = "freddy.orozco@growdata.com.co"
password = "Onagaragardo719???"

# Autenticación
ctx_auth = AuthenticationContext(sharepoint_url)
if ctx_auth.acquire_token_for_user(username, password):
    ctx = ClientContext(sharepoint_url + site_url, ctx_auth)
    file_relative_url = site_url + folder_path + "/" + file_name

    # Creamos un buffer en memoria
    file_obj = BytesIO()

    # Descargamos el archivo al buffer
    ctx.web.get_file_by_server_relative_url(file_relative_url).download(file_obj).execute_query()

    # Leemos el archivo Excel desde el buffer
    file_obj.seek(0)
    df = pd.read_excel(file_obj)

    # Mostramos en Streamlit
    st.title("Archivo Excel desde SharePoint")
    st.dataframe(df)
else:
    st.error("Error de autenticación en SharePoint")
