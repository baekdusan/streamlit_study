# line chart는 altair chart를 간소화 해서 만든 버전
# 복잡한 걸 할 때에는 altair를 사용하는 게 좋음.

import streamlit as st
import pandas as pd
import numpy as np

st.header("st.line_chart")

chart_data = pd.DataFrame(
    np.random.randn(20, 3), # 3축짜리 데이터 20개
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)