import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    '산업공학의 관심 분야가 무엇인가요? 중복 선택이 가능합니다',
    [
        '최적화', '생산관리', '품질관리', '자동화', '데이터 분석', '머신러닝', '딥러닝', '인간공학'
    ],
    default=['최적화', '데이터 분석']
)

st.write(f'선택한 분야는 {", ".join(options)}입니다.')
