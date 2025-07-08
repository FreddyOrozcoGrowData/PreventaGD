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
file_name = "Reporte.xlsx"  # ← cambia por el nombre exacto de tu archivo

username = "tu_correo@growdata.com.co"
password = "tu_contraseña"

# Autenticación
ctx_auth = AuthenticationContext(sharepoint_url)
if ctx_auth.acquire_token_for_user(username, password):
    ctx = ClientContext(sharepoint_url + site_url, ctx_auth)
    file_url = f"{folder_path}/{file_name}"

    response = ctx.web.get_file_by_server_relative_url(site_url + file_url).download()
    ctx.execute_query()

    # Leer el archivo Excel desde memoria
    bytes_file_obj = BytesIO()
    bytes_file_obj.write(response.content)
    bytes_file_obj.seek(0)
    df = pd.read_excel(bytes_file_obj)

    st.dataframe(df)
else:
    st.error("Error de autenticación en SharePoint")
