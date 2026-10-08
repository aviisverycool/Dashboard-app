import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard App")

# Load data
data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D'],
    'values': [10, 20, 30, 40]
})

# Bar chart
fig = px.bar(data, x='category', y='values', title='My Chart')
st.plotly_chart(fig)

# sidebar
option = st.sidebar.selectbox('Choose a category:', data['category'].unique())
st.write(f'You selected: {option}')