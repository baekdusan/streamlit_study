import streamlit as st

st.header('st.checkbox')

st.write('배우고 싶은 과목이 무엇인가요?')

optimization = st.checkbox('최적화')
production_management = st.checkbox('생산관리')
quality_management = st.checkbox('품질관리')
automation = st.checkbox('자동화')
data_analysis = st.checkbox('데이터 분석')
machine_learning = st.checkbox('머신러닝')

if optimization:
    st.write('최적화 수업을 시작합니다.')
if production_management:
    st.write('생산관리 수업을 시작합니다.')
if quality_management:
    st.write('품질관리 수업을 시작합니다.')
if automation:
    st.write('자동화 수업을 시작합니다.')
if data_analysis:
    st.write('데이터 분석 수업을 시작합니다.')
if machine_learning:
    st.write('머신러닝 수업을 시작합니다.')
    
# checkbox는 중복 선택이 가능하다.