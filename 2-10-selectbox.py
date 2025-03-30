import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    '어떤 api를 사용하실 건가요?',
    ('OpenAI', 'Anthropic', 'Gemini')
)

st.write(f'선택한 api는 {option}입니다.')