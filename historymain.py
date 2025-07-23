import streamlit as st
import pandas as pd
from datetime import datetime

# 🔽 원본 데이터 입력 (바로 코드 내에서 처리)
data = {
    "이름": ["안중근", "윤봉길", "이봉창", "김상옥", "유관순", "김구", "안창호", "방정환", "여운형", "권기옥", "남자현", "신채호", "양기탁"],
    "서거연도": ["1910년", "1932년", "1932년", "1923년", "1920년", "1949년", "1938년", "1931년", "1947년", "1988년", "1933년", "1936년", "1938년"],
    "서거일": ["3월 26일", "12월 19일", "10월 10일", "1월 22일", "9월 28일", "6월 26일", "3월 10일", "7월 23일", "7월 19일", "4월 19일", "8월 22일", "2월 21일", "4월 19일"],
    "주요업적": ["이토히로부미 저격", "", "", "", "", "", "", "어린이날 창시자", "", "한국 최초 여성 파일럿", "", "", ""]
}

# ✅ 데이터프레임으로 변환 및 날짜 정제
df = pd.DataFrame(data)
df["월일"] = df["서거일"].str.replace("월 ", "-").str.replace("일", "").str.strip()

# 🖥️ Streamlit 앱 UI
st.title("🇰🇷 독립운동가 서거일 조회")
selected_date = st.date_input("날짜를 선택하세요", datetime.today())
month_day = selected_date.strftime("%-m-%-d")  # 예: '7-23'

# 🎯 일치하는 인물 필터링
matched = df[df["월일"] == month_day]

# 📋 결과 출력
if not matched.empty:
    st.subheader(f"🕯️ {selected_date.strftime('%m월 %d일')}에 서거하신 독립운동가")
    for _, row in matched.iterrows():
        st.markdown(f"""
        **이름**: {row["이름"]}  
        **서거연도**: {row["서거연도"]}  
        **주요업적**: {row["주요업적"] if row["주요업적"].strip() else "정보 없음"}
        """)
else:
    st.info("해당 날짜에 서거한 독립운동가 정보가 없습니다.")
