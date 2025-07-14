import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("postencounterapp.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Post Encounter").sheet1
data = sheet.get_all_records()
df = pd.DataFrame(data)

# App Interface
st.title("📖 Post Encounter Reader")
chapters = df['Chapter'].unique()
selected = st.selectbox("📘 Select a Chapter", chapters)

filtered = df[df['Chapter'] == selected]

for index, row in filtered.iterrows():
    st.subheader(row['Title'])
    st.write(row['Content'])
