import streamlit as st
import pandas as pd
import xlrd

workbook = xlrd.open_workbook("rep-C4A20WV8-210803.xls", ignore_workbook_corruption=True)
df = pd.read_excel(workbook)



st.title("🎈 Casamento Rafa e Giu 🎈 🎉")
st.dataframe(data=df)
