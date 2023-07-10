import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Yari's Company")

"""
## our mission
"""
left_column, right_column = st.columns(2)
button = left_column.button("our mission")
if button:
    right_column.write("we are going to change the world better")

if st.checkbox("show image"):
    img = Image.open("sample.png")
    st.image(img, caption="president Yaginuma message", use_column_width=True)
#use_column_width=True はページの横幅に合わせて表示させる機能

st.sidebar.write("私たちにあなたの情報を教えてください")
name = st.sidebar.text_input("あなたの名前を教えてください。")
age = st.sidebar.selectbox("あなたの年齢を教えてください。", list(range(1,101)))
condition = st.sidebar.slider("当社への期待度を教えてください", 0, 100, 50)

"名前：",name, "様"
"年齢：", age, "歳"
"期待度：", condition ,"％"


st.write("認証待ち")
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"認証率 {i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)



"""
## あなたにオススメのプランを提案します。
"""
df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "２列目": [10, 20, 30, 40]
})
st.dataframe(df, width=1000, height=200)
#st.write(df)ではwidthとheightが使えない
#st.table(df)ではソートができない
#ハイライトしたいときは→ st.write(df.style.highlight_max(axis=0))　

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns= ["R1", "R2", "R3"]
)
#st.line_chart(df)
chart1 = st.expander("過去3年間の営業利益")
chart1.line_chart(df)


df = pd.DataFrame(
    np.random.rand(20, 3),
    columns= ["R1", "R2", "R3"]
)
#st.area_chart(df)
chart1 = st.expander("過去3年間の売上高")
chart1.area_chart(df)


df = pd.DataFrame(
    np.random.rand(20, 3),
    columns= ["R1", "R2", "R3"]
)
#st.bar_chart(df)
chart1 = st.expander("過去3年間の株価")
chart1.bar_chart(df)


st.write("partner list")
df = pd.DataFrame(
    np.random.rand(30, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]
)
st.map(df)