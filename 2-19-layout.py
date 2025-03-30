import streamlit as st

st.set_page_config(layout='wide')

st.title('Streamlit 앱 레이아웃 구성하기')

with st.expander('이 앱에 대하여'):
    st.write('이 앱은 Streamlit을 구성하는 다양한 방법을 보여줍니다.')
    st.image('https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('입력')

user_name = st.sidebar.text_input('당신의 이름은 무엇인가요?')
user_emoji = st.sidebar.selectbox('이모티콘 선택', ['👻', '💩', '👀', '👩‍💻', '🕵🏻‍♂️', '🥳', '🥸', '😴'])
user_food = st.sidebar.multiselect('가장 좋아하는 음식은?', ['치킨', '피자', '치즈볼', '치즈퐁듀', '치즈퐁듀'])

st.header('출력')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 안녕하세요 {user_name}님!')
  else:
    st.write('👈  **이름**을 입력해 주세요!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji}는 당신이 좋아하는 **이모티콘**입니다!')
  else:
    st.write('👈 **이모티콘**을 선택해 주세요!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{", ".join(user_food)}**은 당신이 좋아하는 **음식**입니다!')
  else:
    st.write('👈 가장 좋아하는 **음식**을 선택해 주세요!')
