import streamlit as st

# 페이지 설정
st.set_page_config(page_title="🎥 MBTI 과학/수학 영화 추천기", page_icon="🧠", layout="centered")

# 제목과 설명
st.title("🎬 나의 MBTI로 알아보는 과학·수학 명작 영화")
st.markdown("당신의 성격에 딱 맞는 💡지적이고 🎇흥미로운 영화들을 추천해드릴게요!")

# MBTI 입력
mbti = st.text_input("✍️ 당신의 MBTI를 입력해주세요 (예: INFP, ESTJ 등)", max_chars=4).upper()

# 영화 추천 데이터
recommendations = {
    "INTJ": ["🎥 *Interstellar* - 시공간과 사랑의 과학!", "🧪 *The Imitation Game* - 앨런 튜링의 천재적 사고!", "🔭 *Contact* - 천문학과 철학의 만남"],
    "INFP": ["🎥 *A Beautiful Mind* - 수학자의 삶과 정신", "🧬 *Gattaca* - 유전과 인간다움에 대한 고찰", "🎈 *October Sky* - 꿈을 향한 로켓 발사"],
    "ENTP": ["🎥 *The Theory of Everything* - 호킹의 우주", "📡 *The Man Who Knew Infinity* - 라마누잔의 수학적 여정", "🧠 *Limitless* - 두뇌를 100% 활용한다면?"],
    "ISFJ": ["🎥 *Hidden Figures* - NASA의 숨은 주역들", "📐 *The Martian* - 과학으로 살아남기", "🔬 *Einstein and Eddington* - 물리학의 전환점"],
    "ESTJ": ["🎥 *Apollo 13* - 위기에서 살아남는 원칙과 계획", "📊 *Moneyball* - 통계로 스포츠를 바꾸다", "🛰️ *Gravity* - 냉정한 판단이 생존을 결정한다"],
    "INFJ": ["🎥 *Arrival* - 언어, 시간, 외계생명", "🧠 *Good Will Hunting* - 천재성과 인간관계의 교차점", "🔎 *Proof* - 아버지와 딸, 수학 그리고 진실"],
    "ENFP": ["🎥 *Back to the Future* - 시간여행의 유쾌한 여정", "🧪 *Flubber* - 엉뚱한 발명과 사랑", "🌌 *The Space Between Us* - 지구와 화성, 두 세계의 이야기"],
    "ISTP": ["🎥 *Primer* - 가장 현실적인 타임머신 영화", "🔧 *Iron Man* - 과학과 기술의 화신", "⚙️ *The Martian* - 생존은 문제 해결이다"],
    # 추가 MBTI 유형도 원하시면 이어서 넣을 수 있어요!
}

# 추천 결과
if mbti:
    if mbti in recommendations:
        st.balloons()  # 🎈풍선 효과 터뜨리기
        st.success(f"🎉 {mbti} 유형에게 추천하는 과학/수학 명작 영화는 다음과 같아요:")
        for movie in recommendations[mbti]:
            st.markdown(f"- {movie}")
    else:
        st.warning("🤔 아직 이 MBTI 유형에 대한 데이터가 없어요. 다른 유형을 입력해보세요!")
