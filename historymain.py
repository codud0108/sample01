import streamlit as st
import pandas as pd
from datetime import datetime

# 📁 CSV 불러오기
df = pd.read_csv("independence_heroes.csv")

# 🧹 서거일에서 '월-일'만 추출
df["월일"] = df["서거일"].str.replace("월 ", "-").str.replace("일", "").str.strip()

# 🖥️ 앱 타이틀
st.title("🇰🇷 독립운동가 서거일 조회")

# 📅 날짜 선택
selected_date = st.date_input("날짜를 선택하세요", datetime.today())
month_day = selected_date.strftime("%-m-%-d")

# 🔍 일치하는 데이터 필터링
matched = df[df["월일"] == month_day]

# 📋 결과 출력
if not matched.empty:
    st.subheader(f"🕯️ {selected_date.strftime('%m월 %d일')}에 서거하신 독립운동가")
    for _, row in matched.iterrows():
        st.markdown(f"### 🧑‍🎓 {row['이름']} ({row['서거연도']})")
        with st.expander("주요 업적 펼치기/접기"):
            st.write(row["주요업적"] if pd.notna(row["주요업적"]) and row["주요업적"].strip() else "업적 정보 없음")
else:
    st.info("해당 날짜에 서거한 독립운동가 정보가 없습니다.")
