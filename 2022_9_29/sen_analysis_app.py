import streamlit as st
import pandas as pd
import requests
from transformers import pipeline
from bs4 import BeautifulSoup

classifier = pipeline('sentiment-analysis')
st.title("本日微博關鍵字語意分析")
option = st.selectbox(
    '請選擇想查詢的關鍵字?',
    ('台灣', '兩岸', '蔡英文'))
st.write('您選擇的是:', option)

response = requests.get(
    "https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D{string}".format(string=option))
# st.markdown(response)
soup = BeautifulSoup(response.text, "html.parser")
st.markdown(soup.prettify())
# print(soup.prettify())  #輸出排版後的HTML內容
result = soup.find_all("div", class_="weibo-text", limit=3)
st.markdown(result)
