import streamlit as st

st.title("🌙 수면 도우미 프로그램")

# 프로그램의 단계(Step)를 제어하기 위한 설정
if "step" not in st.session_state:
    st.session_state.step = 1

# [1단계] 취침 정보 입력 (처음에는 여기만 보입니다)
st.subheader("1️⃣ 취침 정보 입력")
current_hour = st.number_input("현재 시간은 몇 시인가요? (0~23 입력)", min_value=0, max_value=23, step=1, key="c_hour")
bed_time = st.number_input("몇 시에 수면을 취할 예정인가요? (0~23 입력)", min_value=0, max_value=23, step=1, key="b_hour")

# 1단계일 때만 [일어나기] 버튼을 보여줌
if st.session_state.step == 1:
    if st.button("⏰ 일어나기"):
        st.session_state.step = 2
        st.rerun()

# [2단계] 기상 정보 입력 ([일어나기] 버튼을 누르면 등장)
if st.session_state.step >= 2:
    st.write("---")
    st.subheader("2️⃣ 기상 정보 입력")
    wake_time = st.number_input("몇 시에 일어났나요? (0~23 입력)", min_value=0, max_value=23, step=1, key="w_hour")
    
    # 2단계일 때만 [결과 확인하기] 버튼을 보여줌
    if st.session_state.step == 2:
        if st.button("📊 결과 확인하기"):
            st.session_state.step = 3
            st.rerun()

# [3단계] 최종 수면 분석 결과 ([결과 확인하기] 버튼을 누르면 등장)
if st.session_state.step == 3:
    st.write("---")
    st.subheader("3️⃣ 수면 분석 결과")
    
    # 조건문(If) 활용: 현재 시간과 취침 시간 비교 경고
    if current_hour >= bed_time:
        st.warning("⚠️ 앗! 현재 시간이 설정한 취침 시간을 넘었습니다. 얼른 주무세요!")
    else:
        st.success("✅ 아직 취침 시간 전이네요. 남은 시간을 잘 마무리하세요.")

    # 조건문(If) 활용: 실제 수면 시간 계산
    if wake_time >= bed_time:
        sleep_duration = wake_time - bed_time
    else:
        sleep_duration = (24 - bed_time) + wake_time

    st.info(f"🛌 **오늘 총 수면 시간**: {sleep_duration}시간")
    st.write("---")
    
    st.write("📋 **오늘의 수면 기록 요약**")
    
    # 리스트(List) 활용: 출력할 데이터를 하나로 묶음
    record_list = [
        f"입력한 현재 시간: {current_hour}시",
        f"설정한 취침 시간: {bed_time}시",
        f"입력한 기상 시간: {wake_time}시",
        f"총 수면 시간: {sleep_duration}시간"
    ]
    
    # 반복문(For) 활용: 리스트 내용을 하나씩 화면에 출력
    for record in record_list:
        st.write(f"- {record}")
        
    # 처음부터 다시 입력할 수 있는 리셋 버튼
    if st.button("🔄 다시 하기"):
        st.session_state.step = 1
        st.rerun()