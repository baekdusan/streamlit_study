import streamlit as st

st.title('st.secrets')

st.write(st.secrets['api_keys']['openai_api_key'])