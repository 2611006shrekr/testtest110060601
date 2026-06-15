import streamlit as st
from datetime import datetime

# 페이지 제목 설정
st.title("🌙 수면 도우미 프로그램")

# [평가 기준 1] 리스트(List) 활용 (3점) - 수면 팁 저장
sleep_tips = [
    "자기 전 30분은 스마트폰 피하기",
    "방의 온도를 시원하게 유지하기",
    "따뜻한 물로 가볍게 샤워하기",
    "내일 할 일을 미리 적어두고 머리 비우기"
]

# 현재 시간 가져오기 (시간 단위만 추출)
current_hour = datetime.now().hour
st.info(f"⏰ 현재 시간은 {current_hour}시입니다.")
st.write("---")

# [평가 기준 2] 입출력 기능 활용 (5점) - st.number_input으로 입력받기
st.subheader("1️⃣ 취침 및 기상 시간 입력")
bed_time = st.number_input("몇 시에 수면을 취할 예정인가요? (0~23 입력)", min_value=0, max_value=23, step=1)
wake_time = st.number_input("몇 시에 일어났나요? (0~23 입력)", min_value=0, max_value=23, step=1)
target_sleep = st.number_input("목표 수면 시간은 몇 시간인가요?", min_value=1, max_value=24, value=8)

st.write("---")

# 버튼을 누르면 결과가 출력되도록 설정
if st.button("결과 확인하기"):
    
    st.subheader("2️⃣ 수면 분석 결과")
    
    # [평가 기준 1] 조건문(If) 활용 (3점) - 현재 시간과 취침 시간 비교
    if current_hour >= bed_time:
        st.warning("⚠️ 앗! 현재 시간이 설정한 취침 시간을 넘었습니다. 얼른 주무세요!")
    else:
        st.success("✅ 아직 취침 시간 전이네요. 남은 시간을 잘 마무리하세요.")

    # 수면 시간 계산 로직 (밤 12시를 넘겨서 자는 경우를 대비한 계산)
    if wake_time >= bed_time:
        sleep_duration = wake_time - bed_time
    else:
        sleep_duration = (24 - bed_time) + wake_time

    st.write(f"🛌 **오늘 총 수면 시간**: {sleep_duration}시간")

    # 조건문 활용 - 목표 수면 시간과 실제 수면 시간 비교
    if sleep_duration >= target_sleep:
        st.success(f"🎉 목표 시간({target_sleep}시간)을 채웠습니다! 개운한 하루 되세요!")
    else:
        lack_of_sleep = target_sleep - sleep_duration
        st.error(f"😢 목표 시간보다 {lack_of_sleep}시간 덜 잤습니다. 피곤할 수 있어요.")
        
        st.write("💡 **부족한 잠을 보충하고 수면의 질을 높이는 팁!**")
        
        # [평가 기준 1] 반복문(For) 활용 (4점) - 리스트에 있는 팁들을 하나씩 출력
        for tip in sleep_tips:
            st.write(f"- {tip}")