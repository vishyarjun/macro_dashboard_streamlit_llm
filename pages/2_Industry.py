import streamlit as st
from reference_data import get_macro_reference_data, get_color_code
import pandas as pd
from yahoo_finance import yfi
import time
import altair as alt

refresh_data=False
industry_data = get_macro_reference_data()


def refresh_industry_data():
    current = 0
    global refresh_data,industry_data
    if not refresh_data:
        progress_text = "Downloading latest sector-wise economic data..."
        my_bar = st.progress(0, text=progress_text)
        
        for row in industry_data.iterrows():
            
            yfi.download_data(row[1]['Symbol'])
            current+=5
            my_bar.progress(current, text=progress_text)

        time.sleep(1)
        my_bar.empty()
    else:
        st.write('latest data already available.')

st.header('Industry-wise Data - :orange[I N] D :green[I A]')

refresh_data = st.button("Refresh Data", type="primary", on_click=refresh_industry_data)
options = st.multiselect(
    label = 'Choose the indicator(s)',
    options = industry_data['Index'],
    placeholder="Choose an option"
    )
df = industry_data
filtered_indices = df.loc[df['Index'].isin(options)]


if len(options) > 0:
    tab1, tab2 = st.tabs(["General", "RSI Comparator"])
    with tab1:
        if len(filtered_indices) > 0:
            for index, row in filtered_indices.iterrows():
                #st.write(row)
                
                st.subheader(body=row['Index'] + ' - ' + row['Sector'],divider="rainbow")
                st.write(row['Description'] + ' ' + row['Investor Usage'])
                graph_data = yfi.graph_data(row['Symbol'])
                chart = alt.Chart(graph_data).mark_line().encode(
                    x='Date:T',
                    y='CLOSE:Q',
                    color=alt.value(get_color_code())  # Set the line color to red
                    ).interactive()
                st.altair_chart(chart, use_container_width=True)

    with tab2:
        all_symbols = filtered_indices['Symbol'].tolist()
        graph_data = yfi.get_custom_graph_data(all_symbols,["RSI14"])
        
        chart2 = alt.Chart(graph_data).mark_line().encode(
                    x='Date:T',
                    y='RSI14:Q',
                    color='Symbol:N',
                    tooltip=['Date:T', 'RSI14:Q', 'Symbol:N'],
                    strokeDash='Symbol'
                    ).interactive().properties(title="Sectorwise RSI")
        
        horizontal_lines = alt.Chart(pd.DataFrame({'value': [30, 70]})).mark_rule().encode(
                                y='value:O',
                                color=alt.Color('value:N', scale=alt.Scale(domain=['30', '70'], range=['green', 'red']))
                                )

        final_chart = alt.layer(chart2, horizontal_lines)

        st.altair_chart(final_chart , use_container_width=True)
        
    
    
