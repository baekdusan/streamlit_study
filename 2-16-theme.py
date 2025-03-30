import streamlit as st

st.title('Streamlit 앱의 테마 사용자 정의하기')

# 기본 테마 설정 보여주기
st.subheader('Streamlit의 기본 테마 설정:')
st.code("""
[theme]
primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
""")

# config.toml 파일의 실제 내용을 읽어서 보여주기
try:
    with open('.streamlit/config.toml', 'r') as f:
        config_content = f.read()
    st.subheader('현재 적용된 `.streamlit/config.toml` 파일의 내용:')
    st.code(config_content)
except FileNotFoundError:
    st.error('config.toml 파일을 찾을 수 없습니다. (기본 테마가 적용됩니다)')
except Exception as e:
    st.error(f'파일을 읽는 중 오류가 발생했습니다: {str(e)}')

number = st.sidebar.slider('숫자를 선택하세요:', 0, 10, 5)
st.write('슬라이더 위젯에서 선택된 숫자:', number)
