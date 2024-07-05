import time

import streamlit as st

import numpy as np
import pandas as pd

st.set_page_config(
   page_title="為啥頭像沒有隨機",
   page_icon="random",
   layout="centered",
   initial_sidebar_state="expanded",
   
   menu_items={
        'Get Help': 'https://blog.jiatool.com/about/',
        'About': "# 這是什麼網頁？ \n**[IT空間](https://blog.jiatool.com/)** 示範 streamlit 之用網頁"
    }
)

bar = st.progress(0)
for i in range(100):
    bar.progress(i + 1, f'目前進度 {i+1} %')
    time.sleep(0.05)

bar.progress(100, '載入完成！')