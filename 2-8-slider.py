# st.slider 함수는 슬라이더를 만들어줌.
# 슬라이더는 숫자를 선택할 수 있는 도구임.
# 슬라이더는 최소값, 최대값, 스텝을 지정할 수 있음.
# 슬라이더는 숫자 외에도 문자열, 불리언, 날짜 등을 선택할 수 있음.

import streamlit as st
from datetime import time, datetime

st.header("st.slider")

st.subheader("Slider")

# 타이틀, 범위, 그리고 기본값을 설정
age = st.slider('당신의 나이는?', 0, 130, 25)
st.write("나는 ", age, "살입니다.")

st.subheader("범위 슬라이더")

values = st.slider(
    '값의 범위를 선택하세요.',
    min_value=0,
    max_value=100,
    value=(25, 75)
)

st.write('선택한 값:', values)

st.subheader("시간 범위 슬라이더")

appointment = st.slider(
    "약속을 예약하세요:",
    value=(time(11, 30), time(12, 45))
)

st.write("예약된 시간:", appointment)

st.subheader("날짜 및 시간 슬라이더")

# 23년 1월 1일 오전 9시 반, 날짜 단위로 변경됨.
start_time = st.slider(
    "언제 시작하시겠습니까?",
    value=datetime(2023, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm"
    # min_value=datetime(2023, 1, 1, 9, 0),
    # max_value=datetime(2023, 1, 1, 10, 0),
    # step=10
)

st.write("시작 시간:", start_time)

