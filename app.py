import streamlit as st
import pandas as pd
import plotly.express as px
from analysis import clean_and_analyze

# Load and process data
df, skill_freq = clean_and_analyze()

st.set_page_config(page_title="📊 Job Market Dashboard", layout="wide")
st.title("📊 Data Science Job Market Dashboard")

# 1️⃣ Top Locations - Bar Chart
st.subheader("📍 Top Job Locations")
top_locations = df['location'].value_counts().head(10).reset_index()
top_locations.columns = ['Location', 'Count']
fig_loc = px.bar(top_locations, x='Location', y='Count', color='Location', title="Top Cities Hiring for Data Science Roles")
st.plotly_chart(fig_loc, use_container_width=True)

# 2️⃣ Top Companies - Pie Chart
st.subheader("🏢 Top Hiring Companies")
top_companies = df['company'].value_counts().head(5).reset_index()
top_companies.columns = ['Company', 'Count']
fig_comp = px.pie(top_companies, names='Company', values='Count', title='Top Hiring Companies by Job Postings', hole=0.4)
st.plotly_chart(fig_comp, use_container_width=True)

# 3️⃣ Top Skills Required - Horizontal Bar Chart
st.subheader("🧠 In-Demand Skills")
skill_df = pd.DataFrame(skill_freq.items(), columns=["Skill", "Frequency"]).sort_values(by='Frequency', ascending=True)
fig_skills = px.bar(skill_df, x='Frequency', y='Skill', orientation='h', color='Skill', title="Most Required Skills")
st.plotly_chart(fig_skills, use_container_width=True)

# 4️⃣ Company-wise Job Count - Treemap
st.subheader("🌲 Company Job Distribution (Treemap)")
fig_treemap = px.treemap(top_companies, path=['Company'], values='Count', title="Hiring Volume by Company (Treemap)")
st.plotly_chart(fig_treemap, use_container_width=True)

# 5️⃣ Location vs Companies - Sunburst Chart
st.subheader("🌞 Job Market Overview (Location → Company)")
sun_df = df.groupby(['location', 'company']).size().reset_index(name='count')
fig_sun = px.sunburst(sun_df, path=['location', 'company'], values='count', title="Jobs by Location and Company")
st.plotly_chart(fig_sun, use_container_width=True)

# 6️⃣ Raw Data
with st.expander("🔍 View Raw Data"):
    st.dataframe(df)


