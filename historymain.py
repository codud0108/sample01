import streamlit as st
import pandas as pd
from datetime import datetime

# 🔽 독립운동가 데이터
people_data = {
    "이름": ["안중근", "윤봉길", "이봉창", "김상옥", "유관순", "김구", "안창호", "방정환", "여운형", "권기옥", "남자현", "신채호", "양기탁","여운홍"],
    "서거연도": ["1910년", "1932년", "1932년", "1923년", "1920년", "1949년", "1938년", "1931년", "1947년", "1988년", "1933년", "1936년", "1938년","1973년"],
    "서거일": ["3월 26일", "12월 19일", "10월 10일", "1월 22일", "9월 28일", "6월 26일", "3월 10일", "7월 23일", "7월 19일", "4월 19일", "8월 22일", "2월 21일", "4월 19일","2월 3일"],
    "주요업적": ["이토히로부미 저격", "", "", "", "", "", "", "어린이날 창시자", "", "한국 최초 여성 파일럿", "", "", "","파리 강화회의 참석, 임시정부의정원 의원, 태평양전쟁이후 변절"]
}
people_df = pd.DataFrame(people_data)
people_df["월일"] = people_df["서거일"].str.replace("월 ", "-").str.replace("일", "").str.strip()

# 🔽 독립운동 사건 데이터
event_data = {
    "독립운동이름": ["3.1 운동", "광주학생운동", "봉오동 전투", "청산리 대첩", "한인애국단 창단"],
    "발생날짜": ["3월 1일", "11월 3일", "6월 7일", "10월 21일", "12월 10일"],
    "간단설명": [
        "1919년, 전국에서 비폭력 독립만세운동이 일어남",
        "1929년, 광주 학생들이 일본인 교사와의 갈등을 계기로 일제에 항거함",
        "1920년, 홍범도 장군이 이끄는 독립군이 일본군에 대승",
        "1920년, 김좌진 장군이 주도한 독립군 최대 전투",
        "1931년 김구가 조직한 항일 테러 단체"
    ]
}
events_df = pd.DataFrame(event_data)
events_df["월일"] = events_df["발생날짜"].str.replace("월 ", "-").str.replace("일", "").str.strip()

# 🖥️ Streamlit UI
st.title("📅 생일에 일어난 역사 알아보기")
selected_date = st.date_input("날짜를 선택하세요", datetime.today())
month_day = selected_date.strftime("%-m-%-d")  # ex) '3-1'

# 🕯️ 서거한 독립운동가 출력
matched_people = people_df[people_df["월일"] == month_day]
if not matched_people.empty:
    st.subheader(f"🕯️ {selected_date.strftime('%m월 %d일')} 서거한 독립운동가")
    for _, row in matched_people.iterrows():
        st.markdown(f"**이름**: {row['이름']}  \n**서거연도**: {row['서거연도']}")
        with st.expander("주요 업적 펼치기/접기"):
            st.write(row["주요업적"] if row["주요업적"].strip() else "정보 없음")
else:
    st.info("해당 날짜에 서거한 독립운동가 정보가 없습니다.")

# 🔥 독립운동 사건 출력
matched_events = events_df[events_df["월일"] == month_day]
if not matched_events.empty:
    st.subheader(f"🔥 {selected_date.strftime('%m월 %d일')} 일어난 독립운동 사건")
    for _, row in matched_events.iterrows():
        st.markdown(f"**{row['독립운동이름']}**  \n📆 {row['발생날짜']}  \n📝 {row['간단설명']}")
else:
    st.info("해당 날짜에 일어난 독립운동 사건 정보가 없습니다.") 
