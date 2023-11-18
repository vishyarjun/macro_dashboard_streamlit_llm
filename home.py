import streamlit as st
from imf_interface import imf
from typing import List
from color_codes import get_color_code
import altair as alt


options = []
results = []
descriptions = []


indicators = imf.get_all_indicators(True)
st.set_page_config(layout='wide')
st.header('Macroeconomic Indicators - :orange[I N] D :green[I A]')
options = st.multiselect(
    label = 'Choose the indicator(s)',
    options = list(indicators.keys()),
    placeholder="Choose an option",
    default = "Real GDP growth"
    )
if len(options) > 0:
    for opt in options:
        results.append(indicators[opt][0])
        descriptions.append(indicators[opt][1])
    graph_data = imf.get_graph_data(results)
    
    for i,opt in enumerate(results):
        st.subheader(body=options[i],divider="rainbow")
        st.write(descriptions[i])
        chart = alt.Chart(graph_data).mark_line().encode(
            x='Year:O',
            y=opt,
            color=alt.value(get_color_code())  # Set the line color to red
            ).interactive()
        st.altair_chart(chart, use_container_width=True)