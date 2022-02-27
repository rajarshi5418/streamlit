import pynse
from pynse import*
import datetime
import logging
import streamlit as st

nse = pynse.Nse()

list_index=dir(IndexSymbol)
for i in list_index:
    st.text(i)
    index = eval("IndexSymbol"+"."+i)
    try:
        data=nse.top_gainers(index).head(7)
        st.dataframe(data['pChange'])
        # print(data.columns)
    except ValueError:
        st.text("sorry")


