# main.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# 1. 웹 페이지 설정
st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

st.title("2026 학교 등산 행사 안내 지도")
st.markdown("**강조** *이탤릭체*")
st.markdown("# 큰 제목")
st.markdown("## 작은 제목")
st.text("안녕^-^")

st.code("a=3")

#데이터 읽어오기(데이터 수집 csv)
df = pd.read_csv('인천광역시 남동구_고등학교_20240325.csv', encoding = 'cp949')
df_latlon = df[['위도','경도']]
df_latlon = df_latlon.rename(columns={'위도':'lat','경도':'lon'})
st.map(df_latlon)

# 지도 생성 및 마커 표시(시각화 단계)
m = folium.Map(
    location=[
37.404160, 126.719249],
    zoom_start=12
)
folium.Marker(
      location=[37.404160, 126.719249],
      popup = "클릭해보세요"
      tooltip= "남동고등학교", 
      icon = folium.Icon(color='purple', icon='info-sign')
  ).add_to(m)
