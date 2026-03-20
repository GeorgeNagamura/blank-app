import streamlit as st
import pandas as pd
import xlrd

workbook = xlrd.open_workbook("rep-C4A20WV8-210803.xls", ignore_workbook_corruption=True)
df = pd.read_excel(workbook)
karaoke_df = df[["Interprete","Nome","Codigo","Trecho","Idioma"]]
karaoke_df["Nome"].str.upper()

def limpar_selecao():
    st.session_state["search"] = ""

def search_item(karaoke_df):
    if query:
        filtered_df = karaoke_df[karaoke_df.astype(str).apply(lambda x: x.str.contains(query, case=False)).any(axis=1)]
        karaoke_df = filtered_df

st.title("🎈 Casamento Rafa e Giu 🎈 🎉")

query = st.text_input("PROCURAR NA LISTA", key="search").upper()
if query:
    filtered_df = karaoke_df[karaoke_df.astype(str).apply(lambda x: x.str.contains(query, case=False)).any(axis=1)]
    karaoke_df = filtered_df

col1, col2, col3 = st.columns([0.7,0.15,0.15])
with col2:
    st.button('Limpar', on_click=limpar_selecao)
with col3:
    st.button('Procurar', on_click=search_item, args=[karaoke_df])

st.write('TODAS AS MÚSICAS')
st.dataframe(data=karaoke_df, width="stretch", hide_index=True)

