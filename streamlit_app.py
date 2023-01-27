import streamlit as st
import pandas as pd

if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Template",
                    page_icon='✅',
                    initial_sidebar_state='collapsed')
    df = pd.read_csv("hei.csv")
    st.line_chart(df)


