import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Example data (replace this with your RSI data)
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
rsi_values = np.random.uniform(0, 100, len(date_rng))
symbols = np.random.choice(['A', 'B', 'C'], len(date_rng))
graph_data = pd.DataFrame({'Date': date_rng, 'RSI14': rsi_values, 'Symbol': symbols})

# Create the Altair chart
chart2 = alt.Chart(graph_data).mark_line().encode(
    x='Date:T',
    y='RSI14:Q',
    color='Symbol:N',
    tooltip=['Date:T', 'RSI14:Q', 'Symbol:N'],
    strokeDash='Symbol'
).interactive().properties(title="Sectorwise RSI")

# Add horizontal lines at 30 and 70 using layer
horizontal_lines = alt.Chart(pd.DataFrame({'value': [30, 70]})).mark_rule().encode(
    y='value:O',
    color=alt.Color('value:N', scale=alt.Scale(domain=['30', '70'], range=['green', 'red']))
)

# Combine the chart and lines
final_chart = alt.layer(chart2, horizontal_lines)

# Display the chart using Streamlit
st.altair_chart(final_chart, use_container_width=True)
