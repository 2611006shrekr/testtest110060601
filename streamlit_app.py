import streamlit as st

st.title("🌙 수면 도우미 프로그램")

st.subheader("1️⃣ 취침 정보 입력")
# 처음 켰을 때 바로 경고가 뜨지 않도록 기본값(value)을 각각 21시와 23시로 줍니다.
current_hour = st.number_input("현재 시간은 몇 시인가요? (0~23 입력)", min_value=0, max_value=23, value=21, step=1)
bed_time = st.number_input("몇 시에 수면을 취할 예정인가요? (0~23 입력)", min_value=0, max_value=23, value=23, step=1)

# [조건문] 입력하는 순간 실시간으로 비교하여 화면에 메시지를 계속 유지합니다.
if current_hour >= bed_time:
    st.warning("⚠️ 앗! 현재 시간이 설정한 취침 시간을 넘었습니다. 얼른 주무세요!")
else:
    st.success("✅ 아직 취침 시간 전이네요. 남은 시간을 잘 마무리하세요.")

st.write("---")

# 기상 정보 입력창을 제어하기 위한 변수
if "woke_up" not in st.session_state:
    st.session_state.woke_up = False

# [일어나기] 버튼
if st.button("⏰ 일어나기"):
    st.session_state.woke_up = True

# [일어나기] 버튼을 누른 후에만 아래 기상 정보와 요약 리스트가 나타납니다.
if st.session_state.woke_up:
    st.subheader("2️⃣ 기상 정보 입력 및 결과")
    wake_time = st.number_input("몇 시에 일어났나요? (0~23 입력)", min_value=0, max_value=23, value=7, step=1)
    
    # [조건문] 수면 시간 계산
    if wake_time >= bed_time:
        sleep_duration = wake_time - bed_time
    else:
        sleep_duration = (24 - bed_time) + wake_time

    st.info(f"🛌 **오늘 총 수면 시간**: {sleep_duration}시간")
    st.write("---")
    
    st.write("📋 **오늘의 수면 기록 요약**")
    
    # [리스트] 수행평가 필수 조건 채우기
    record_list = [
        f"입력한 현재 시간: {current_hour}시",
        f"설정한 취침 시간: {bed_time}시",
        f"입력한 기상 시간: {wake_time}시",
        f"총 수면 시간: {sleep_duration}시간"
    ]
    
    # [반복문] 수행평가 필수 조건 채우기
    for record in record_list:
        st.write(f"- {record}")