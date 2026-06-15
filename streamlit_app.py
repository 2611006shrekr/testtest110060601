import streamlit as st
from datetime import datetime

st.title("🌙 수면 도우미 프로그램")

current_hour = datetime.now().hour
st.info(f"⏰ 현재 시간은 {current_hour}시입니다.")
st.write("---")

st.subheader("1️⃣ 취침 및 기상 시간 입력")
bed_time = st.number_input("몇 시에 수면을 취할 예정인가요? (0~23 입력)", min_value=0, max_value=23, step=1)
wake_time = st.number_input("몇 시에 일어났나요? (0~23 입력)", min_value=0, max_value=23, step=1)
target_sleep = st.number_input("목표 수면 시간은 몇 시간인가요?", min_value=1, max_value=24, value=8)

st.write("---")

if st.button("결과 확인하기"):
    
    st.subheader("2️⃣ 수면 분석 결과")
    
    # 현재 시간과 취침 시간 비교
    if current_hour >= bed_time:
        st.warning("⚠️ 앗! 현재 시간이 설정한 취침 시간을 넘었습니다. 얼른 주무세요!")
    else:
        st.success("✅ 아직 취침 시간 전이네요. 남은 시간을 잘 마무리하세요.")

    # 수면 시간 계산
    if wake_time >= bed_time:
        sleep_duration = wake_time - bed_time
    else:
        sleep_duration = (24 - bed_time) + wake_time

    st.write(f"🛌 **오늘 총 수면 시간**: {sleep_duration}시간")

    # 목표 수면 시간과 실제 수면 시간 비교
    if sleep_duration >= target_sleep:
        st.success(f"🎉 목표 시간({target_sleep}시간)을 채웠습니다! 개운한 하루 되세요!")
    else:
        lack_of_sleep = target_sleep - sleep_duration
        st.error(f"😢 목표 시간보다 {lack_of_sleep}시간 덜 잤습니다. 피곤할 수 있어요.")
        
    st.write("---")
    st.write("📋 **오늘의 수면 기록 요약**")
    
    # 리스트와 반복문 필수 조건 충족을 위한 요약 데이터 출력
    record_list = [
        f"설정한 취침 시간: {bed_time}시",
        f"입력한 기상 시간: {wake_time}시",
        f"총 수면 시간: {sleep_duration}시간",
        f"목표 수면 시간: {target_sleep}시간"
    ]
    
    for record in record_list:
        st.write(f"- {record}")