import streamlit as st

st.write("st.write")

st.write("Hello, *World* :sunglasses:") # 이렇게 하면 글자 모양이 바뀌고 이모지도 나옴

st.write(1234) # 숫자도 나옴

st.write(1234.5678) # 소수점도 나옴

import pandas as pd
import altair as alt

df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})

st.write("Below is a DataFrame:", df, "Above is a DataFrame.") # 위, 아래로 설명 넣어주기.

import numpy as np

df2 = pd.DataFrame(
    # 랜덤으로 20개의 데이터를 3개의 열로 만들어줌.
    # [[3, 14, 123] * 20] 이렇게 20개의 데이터가 들어감.
    np.random.randn(20, 3),
    # 열의 이름을 a, b, c로 지정
    columns=['a', 'b', 'c']
)

# alt는 데이터 시각화 라이브러리
# mark_circle는 원 모양으로 시각화
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)

st.write(c)
