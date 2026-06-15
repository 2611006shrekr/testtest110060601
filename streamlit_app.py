import streamlit as st

st.title("🌙 수면 도우미 프로그램")

st.subheader("1️⃣ 취침 정보 입력")
current_hour = st.number_input("현재 시간은 몇 시인가요? (0~23 입력)", min_value=0, max_value=23, step=1)
bed_time = st.number_input("몇 시에 수면을 취할 예정인가요? (0~23 입력)", min_value=0, max_value=23, step=1)

if current_hour >= bed_time:
    st.warning("⚠️ 앗! 현재 시간이 설정한 취침 시간을 넘었습니다. 얼른 주무세요!")
else:
    st.success("✅ 아직 취침 시간 전이네요. 남은 시간을 잘 마무리하세요.")

st.write("---")

if "woke_up" not in st.session_state:
    st.session_state.woke_up = False

if st.button("⏰ 일어나기"):
    st.session_state.woke_up = True

if st.session_state.woke_up:
    st.subheader("2️⃣ 기상 정보 입력")
    wake_time = st.number_input("몇 시에 일어났나요? (0~23 입력)", min_value=0, max_value=23, step=1)
    
    if wake_time >= bed_time:
        sleep_duration = wake_time - bed_time
    else:
        sleep_duration = (24 - bed_time) + wake_time

    st.success(f"🛌 **오늘 총 수면 시간**: {sleep_duration}시간")
    
    st.write("📋 **오늘의 수면 기록 요약**")
    
    record_list = [
        f"입력한 현재 시간: {current_hour}시",
        f"설정한 취침 시간: {bed_time}시",
        f"입력한 기상 시간: {wake_time}시",
        f"총 수면 시간: {sleep_duration}시간"
    ]
    
    for record in record_list:
        st.write(f"- {record}")