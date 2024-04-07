import streamlit as st
import pandas as pd
import numpy as np

st.title("emorin's train page")
st.header('こんにちは 世界')

st.markdown('''
こんにちは！

これはStreamlitMultiPageAppのテストです。
''')

st.image("asset/勇気りんりん.jpg")

# *** sidebar
st.sidebar.title('これは home のサイドバーだよ')
st.sidebar.image('asset\Give&Grow.jpg', use_column_width=True)