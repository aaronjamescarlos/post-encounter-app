
import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("postencounterapp-c519a9aed711.json", scope)
client = gspread.authorize(creds)

# Load data
sheet = client.open("Post Encounter").sheet1
data = sheet.get_all_records()
df = pd.DataFrame(data)

# App UI
st.title("📖 Post Encounter Articles")

# Group and filter chapters
if 'Chapter' in df.columns:
    chapters = df['Chapter'].unique()
    selected = st.selectbox("📘 Select a Chapter", chapters)
    filtered = df[df['Chapter'] == selected]
    for i, row in filtered.iterrows():
        st.subheader(row.get("Title", f"Article {i+1}"))
        st.write(row.get("Content", "No content found."))
else:
    st.error("❌ 'Chapter' column not found in your Google Sheet.")
