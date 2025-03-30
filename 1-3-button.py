import streamlit as st

st.header("버튼 클릭하면 메시지 나오게 하기")

hello_button = st.button("Say Hello") # 이렇게 해도 button의 초기 설정은 false임.

if hello_button:
    st.write("Why hello there")
else:
    st.write("Goodbye")
