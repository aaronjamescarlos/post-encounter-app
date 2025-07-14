import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Google Sheets Setup using Streamlit secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = st.secrets["gcp_service_account"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(dict(creds_dict), scope)
client = gspread.authorize(creds)

# Load data
sheet = client.open("Post Encounter").sheet1
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Streamlit app
st.title("📖 Post Encounter Articles")
chapters = df['Chapter'].unique()
selected = st.selectbox("📘 Select a Chapter", chapters)
filtered = df[df['Chapter'] == selected]
st.write(filtered)
