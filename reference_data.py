# color_codes.py
import random
import csv
import pandas as pd
color_codes = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
    "#aec7e8", "#ffbb78", "#98df8a", "#ff9896", "#c5b0d5",
    "#c49c94", "#f7b6d2", "#c7c7c7", "#dbdb8d", "#9edae5",
    "#393b79", "#5254a3", "#6b6ecf", "#9c9ede", "#637939",
    "#8ca252", "#b5cf6b", "#cedb9c", "#8c6d31", "#bd9e39",
    "#e7ba52", "#e7cb94", "#843c39", "#ad494a", "#d6616b",
    "#e7969c", "#7b4173", "#a55194", "#ce6dbd", "#de9ed6",
    "#8dd3c7", "#ffffb3", "#bebada", "#fb8072", "#80b1d3",
    "#fdb462", "#b3de69", "#fccde5", "#d9d9d9", "#bc80bd",
    "#ccebc5", "#ffed6f", "#737373", "#969696", "#bcbcbc",
    "#d9d9d9", "#fdae61", "#fee08b", "#d73027", "#4575b4",
    "#91bfdb", "#313695", "#a50026", "#fee08b", "#d73027",
    "#4575b4", "#91bfdb", "#313695", "#a50026", "#e7298a",
    "#66a61e", "#e6ab02", "#d95f02", "#1b9e77", "#d95f02",
    "#1b9e77", "#d95f02", "#1b9e77", "#d95f02", "#1b9e77",
    "#d95f02", "#1b9e77", "#d95f02", "#1b9e77", "#d95f02",
    "#1b9e77", "#d95f02", "#1b9e77", "#d95f02", "#1b9e77",
    "#d95f02", "#1b9e77", "#d95f02", "#1b9e77", "#d95f02"
]

def get_color_code():
    return random.choice(color_codes)


macroeconomic_indicators = [
    "NGDP_RPCH",
    "PCPIPCH",
    "LUR",
    "BCA_NGDPD",
    "exp",
    "GGXCNL_GDP",
    "BX_GDP",
    "BM_GDP",
    "BFD_GDP",
    "FMB_PCH",
    "EREER",
    "PCPI_PCH",
    "DG_GDP",
    "BRASS_MI"
]

def get_macro_reference_data():
    file_path = './data/ref_macro.csv'
    df = pd.read_csv(file_path, encoding='utf-8')
    return df

