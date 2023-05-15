# ----------------
# 基本設定
# ----------------
# ライブラリ読み込み
import streamlit as st

st.title('おなすバイバイン')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('おなすを増やす')
if increment:
    if st.session_state.count == 0:
        st.session_state.count = 1
    else:
        st.session_state.count = st.session_state.count * 2
reset_button = st.button('リセット')
if reset_button:
    st.session_state.count = 0

num = st.session_state.count
double = num * 2
st.write('Count🍆 = ', double)


st.write('🍆'*double)
