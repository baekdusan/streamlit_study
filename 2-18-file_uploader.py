import streamlit as st
import pandas as pd

st.title('st.file_uploader')

st.subheader('CSV 파일 업로드')

uploaded_file = st.file_uploader('파일 선택', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.subheader('기술 통계')
    st.write(df.describe())
else: # 파일이 업로드 되지 않았을 때
    st.info('CSV 파일을 업로드 해주세요.')

