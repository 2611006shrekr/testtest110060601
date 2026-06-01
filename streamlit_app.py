import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="자기소개 포트폴리오",
    page_icon="👋",
    layout="wide"
)
 
# --- 사이드바 (연락처 및 링크) ---
st.sidebar.header("📬 Contact Me")
st.sidebar.info(
    """
    - **Email:** your.email@example.com
    - **GitHub:** [github.com/yourusername](https://github.com/yourusername)
    - **LinkedIn:** [linkedin.com/in/yourusername](https://www.linkedin.com/in/yourusername)
    - **Blog:** [yourblog.com](https://yourblog.com)
    """
)
st.sidebar.write("---")
st.sidebar.write("💡 *이 페이지는 Streamlit으로 제작되었습니다.*")

# --- 메인 타이틀 ---
st.title("안녕하세요! 🧑‍💻 [본인 이름]의 포트폴리오입니다.")
st.write("#### 끊임없이 배우고 성장하는 것을 즐기는 [직무/포지션]입니다.")
st.write("---")

# --- 탭(Tabs)을 이용한 섹션 분리 ---
tab1, tab2, tab3 = st.tabs(["💡 About Me", "🛠️ Tech Stack", "🚀 Projects"])

# 1. About Me 탭
with tab1:
    st.header("About Me")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 사진이 있다면 경로를 넣어주세요. 없다면 이모지로 대체 가능합니다.
        # st.image("profile.jpg", width=250)
        st.write("📸 (여기에 프로필 사진을 넣을 수 있습니다)")
        
    with col2:
        st.write("""
        저는 데이터를 분석하고 시각화하여 새로운 인사이트를 얻는 것을 좋아합니다. 
        항상 사용자 관점에서 생각하며, 효율적이고 깔끔한 코드를 작성하기 위해 노력합니다.
        
        - **학력:** OO대학교 OO학과 졸업 (202X.02)
        - **자격증:** 정보처리기사, SQLD 등
        - **관심 분야:** 데이터 분석, 웹 개발, 인공지능
        """)

# 2. Tech Stack 탭
with tab2:
    st.header("Tech Stack")
    
    col_lang, col_frame, col_tools = st.columns(3)
    
    with col_lang:
        st.subheader("Languages")
        st.write("- Python ⭐⭐⭐")
        st.write("- SQL ⭐⭐⭐")
        st.write("- JavaScript ⭐⭐")
        
    with col_frame:
        st.subheader("Frameworks/Libs")
        st.write("- Streamlit")
        st.write("- Pandas / NumPy")
        st.write("- Django")
        
    with col_tools:
        st.subheader("Tools")
        st.write("- Git / GitHub")
        st.write("- Docker")
        st.write("- AWS")

# 3. Projects 탭
with tab3:
    st.header("Projects")
    
    # 프로젝트 1 (확장/축소 가능한 Expander 사용)
    with st.expander("🥇 프로젝트 1: 대기오염 데이터 분석 대시보드 (202X.XX ~ 202X.XX)"):
        st.write("**📝 설명:** 공공데이터포털의 API를 활용하여 지역별 대기오염 수치를 시각화한 대시보드입니다.")
        st.write("**🛠️ 사용 기술:** Python, Streamlit, Pandas, Plotly")
        st.write("**🔗 링크:** [GitHub Repository](#)")
        
    # 프로젝트 2
    with st.expander("🥈 프로젝트 2: 머신러닝 기반 주가 예측 모델 (202X.XX ~ 202X.XX)"):
        st.write("**📝 설명:** 과거 주식 데이터를 바탕으로 내일의 주가를 예측하는 LSTM 모델을 구축했습니다.")
        st.write("**🛠️ 사용 기술:** Python, TensorFlow, Scikit-learn")
        st.write("**🔗 링크:** [GitHub Repository](#)")