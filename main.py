# main.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# 1. 웹 페이지 설정
st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

# 2. 데이터 읽어오기(데이터 수집 csv)
# df = pd.read_csv('등산경로.csv', encoding = 'utf-8')
# 코스의 위치에 해당하는 사진 이미지 이름 : "images/A입구.jpg"
df = pd.read_csv('등산경로.csv', encoding = 'utf-8')
df['이미지'] = 'images/'+ df['코스'] + df['위치명'] + '.jpg'
df_latlon = df[['위도','경도']]
df_latlon = df_latlon.rename(columns={'위도':'lat','경도':'lon'})
# st.map(df_latlon)

# 3. 지도 생성 및 마커 표시(시각화 단계)
m = folium.Map(
    location=[
37.405969, 126.721529],
    zoom_start=15
)
"""
folium.Marker(
    location=[37.404160, 126.719249],
    popup = "ㅁㅁㅁ",
    tooltip= "남동고등학교", 
    icon = folium.Icon(color='purple', icon='info-sign')
).add_to(m)
"""
for i in range(len(df)):
    folium.Marker(
        location=[df.iloc[i]['위도'], df.iloc[i]['경도']],
        popup = f'<div style = "width:150px"> </strong>{df.iloc[i]['위치명']}</strong></div>',
        tooltip= "나를 클릭하세요", 
        icon = folium.Icon(color='purple', icon='info-sign')
    ).add_to(m)

# 4.화면 출력
col1, col2 = st.columns([3,1])
with col1:
    st_folium(m, width=700, height=500)
with col2:
    st.subheader("정보") #코스정보
    st.info("길이 미끄럽습니다. 주의하세요.")
    st.metric(label="소요시간", value="10분")
    st.write("주의사항 : 등산화를 착용하세요.(●'◡'●)")
st_folium(m, width=700, height=500)
