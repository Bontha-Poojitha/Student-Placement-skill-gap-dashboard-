import streamlit as st
import pandas as pd

st.title("Student Placement Skill Gap Dashboard")

df = pd.read_csv("placement_data.csv")
st.write(df)

st.subheader("Placed vs Not Placed")
st.bar_chart(df['Placed'].value_counts())

st.subheader("Average Package by Company")
st.bar_chart(df.groupby('Company')['Package'].mean())
