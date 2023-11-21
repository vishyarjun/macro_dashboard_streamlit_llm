import altair as alt
from vega_datasets import data
import streamlit as st

source = data.stocks()
st.write(source)
base = alt.Chart(source).encode(
    alt.Color("symbol").legend(None)
).transform_filter(
    "datum.symbol !== 'IBM'"
).properties(
    width=500
)

line = base.mark_line().encode(x="date", y="price")


last_price = base.mark_circle().encode(
    alt.X("last_date['date']:T"),
    alt.Y("last_date['price']:Q")
).transform_aggregate(
    last_date="argmax(date)",
    groupby=["symbol"]
)

company_name = last_price.mark_text(align="left", dx=4).encode(text="symbol")

chart = (line + last_price + company_name).encode(
    x=alt.X().title("date"),
    y=alt.Y().title("price")
)

st.altair_chart(chart, use_container_width=True)
