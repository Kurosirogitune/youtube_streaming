import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title('streamlit 入門')
st.write('プログレスバー')
'Start!!'

#latest_iteration = st.empty()
#bar = st.progress(0)
#for i in range(100):
#    latest_iteration.text(f'Iteration {i+1}')
#    bar.progress(i + 1)
#    time.sleep(0.1)

#'Done!!!!'


left_column,right_column =st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここが右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容')

text = st.text_input('あなたの趣味を教えてください')
condition = st.slider('あなたの調子は',0,100,50)

'私のシュミは',text
'私の調子は', condition

#セレクトボックスの中から好きな文字を選んで代入
#text = st.text_input('あなたの趣味を教えてください')
#'私のシュミは',text
#スライダーで数値をいじる
#condition = st.slider('あなたの調子は',0,100,50)
#'私の調子は', condition

#セレクトボックスの中から数値を選んで文字に代入
option = st.selectbox(
    'あなたが好きな数字',
    list(range(1,11))
)
'あなたの好きな数字は',option,'です'

#チェックボックスにチェックを入れると画像表示
if st.checkbox('Show Image'):
    img = Image.open('starwars.png')
    st.image(img,caption='スターウォーズ',use_column_width=True)

#マッピング姫路城#割り算した小さい値に姫路城の緯度経度を基にマッピングする
 df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [34.83,134.69],
    columns=['lat','lon']#緯度 #経度
)
st.map(df) 


