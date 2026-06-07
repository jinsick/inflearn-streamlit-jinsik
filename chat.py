import streamlit as st
from dotenv import load_dotenv
from llm import get_ai_response

load_dotenv()

st.set_page_config(
    page_title="법인세 AI 상담 시스템",
    page_icon="⚖️",
    layout="centered",
)

st.markdown("""
<style>
/* =====================================================
   CTB = Corporate Tax Bot
   라이트/다크 모두 동작: rgba 투명도 + CSS 변수 기반
   ===================================================== */

/* ── CTB-01: 메인 컨텐츠 너비 ── */
.block-container {
    max-width: 800px !important;
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
}

/* ── CTB-02: 사이드바 배경 ── */
[data-testid="stSidebar"] {
    background-color: #1B3A6B;
}
/* 사이드바 모든 텍스트 요소 — 라이트/다크 공통으로 밝은 색 강제 */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] li,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] strong,
[data-testid="stSidebar"] em,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .stMarkdown li,
[data-testid="stSidebar"] .stMarkdown h3 {
    color: #E2ECF8 !important;
}
/* 사이드바 구분선 */
[data-testid="stSidebar"] hr {
    border-color: rgba(255, 255, 255, 0.2) !important;
}
/* 사이드바 h3 하단 여백 축소 */
[data-testid="stSidebar"] h3 {
    margin-bottom: 4px !important;
}
/* 사이드바 stMarkdown 패딩 축소 */
[data-testid="stSidebar"] [data-testid="stMarkdown"] {
    padding-top: 0px !important;
    padding-bottom: 0px !important;
}
[data-testid="stSidebar"] [data-testid="stMarkdown"] > div {
    padding-top: 0px !important;
    padding-bottom: 0px !important;
}
[data-testid="stSidebar"] [data-testid="stMarkdown"] p {
    margin-top: 2px !important;
    margin-bottom: 2px !important;
    line-height: 1.5 !important;
}

/* ── CTB-02a: 사이드바 버튼 — 라이트/다크 공통, 어두운 배경에 밝은 텍스트 ── */
[data-testid="stSidebar"] button {
    background-color: rgba(255, 255, 255, 0.12) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
}
[data-testid="stSidebar"] button span,
[data-testid="stSidebar"] button span span {
    color: #E2ECF8 !important;
}

/* ── CTB-02b: 사이드바 안내사항 텍스트 크기 ── */
.ctb-sidebar-guide p,
.ctb-sidebar-guide li {
    font-size: 15px !important;
    color: #E2ECF8 !important;
    line-height: 1.65 !important;
    margin-top: 3px !important;
    margin-bottom: 3px !important;
}
.ctb-sidebar-guide strong {
    color: #E2ECF8 !important;
    font-size: 15px !important;
}

/* ── CTB-03: 헤더 카드 — 사이드바와 동일한 배경색 적용 ── */
.ctb-header-card {
    background-color: #1B3A6B;
    border-radius: 12px 12px 0 0;
    border: 1.5px solid rgba(27, 58, 107, 0.8);
    border-top: none;
    border-bottom: none;
    padding: 44px 32px 18px 32px;
    box-shadow: 0 2px 12px rgba(27, 58, 107, 0.35);
}
.ctb-header-top {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 14px;
}
.ctb-header-icon {
    width: 52px;
    height: 52px;
    background: linear-gradient(135deg, #2C5AA0 0%, #5B8DD9 100%);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.6rem;
    flex-shrink: 0;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}
.ctb-header-title {
    color: #FFFFFF !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
    margin: 0 0 8px 0 !important;
    line-height: 1.2 !important;
    letter-spacing: -0.3px !important;
}
.ctb-header-subtitle {
    color: rgba(226, 236, 248, 0.75) !important;
    font-size: 1.08rem !important;
    margin: 0 !important;
}
.ctb-header-divider {
    border: none;
    border-top: 1px solid rgba(255, 255, 255, 0.18);
    margin: 0 0 12px 0;
}

/* ── CTB-04: 배지 — 다크 헤더 배경 위 밝은 스타일 ── */
.ctb-badge-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}
.ctb-badge {
    background: rgba(255, 255, 255, 0.12);
    color: #E2ECF8;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.2px;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.15);
}

/* ── CTB-05: 본문 안내 카드 ── */
.ctb-body-card {
    background-color: var(--secondary-background-color);
    border-radius: 0 0 12px 12px;
    border: 1.5px solid rgba(128, 128, 128, 0.45);
    border-top: none;
    border-left: 4px solid #2C5AA0;
    padding: 18px 28px 20px 28px;
    margin-bottom: 16px;
    box-shadow: 0 2px 12px rgba(44, 90, 160, 0.06);
}

/* ── CTB-06: 안내 텍스트 ── */
.ctb-guide-text {
    color: var(--text-color);
    opacity: 0.75;
    font-size: 0.87rem;
    margin: 0;
    line-height: 1.7;
}

/* ── CTB-07: 채팅 메시지 버블 ── */
[data-testid="stChatMessage"] {
    border-radius: 10px;
    border: 1.5px solid rgba(128, 128, 128, 0.35);
    margin-bottom: 8px;
    box-shadow: 0 1px 6px rgba(0, 0, 0, 0.08);
    background-color: var(--secondary-background-color);
}

/* ── CTB-08: 채팅 입력창 ── */
[data-testid="stChatInput"] textarea {
    color: var(--text-color) !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: rgba(128, 128, 128, 0.6) !important;
}

/* ── CTB-09: expander 본문 텍스트 ── */
[data-testid="stExpanderDetails"] p,
[data-testid="stExpanderDetails"] li {
    color: var(--text-color) !important;
}

/* ── CTB-10: 푸터 ── */
.ctb-footer {
    text-align: center;
    color: var(--text-color);
    opacity: 0.45;
    font-size: 0.73rem;
    margin-top: 20px;
    padding-top: 14px;
    border-top: 1px solid rgba(128, 128, 128, 0.15);
    line-height: 1.7;
}

/* ── CTB-11: 예시 질문 텍스트 ── */
.ctb-examples-text {
    color: var(--text-color);
    font-size: 0.87rem;
    line-height: 1.55;
    opacity: 0.8;
    padding: 2px 0;
}
</style>
""", unsafe_allow_html=True)

# ── 사이드바 ──────────────────────────────────────────
with st.sidebar:
    st.markdown("""
### ⚖️ 법인세 AI 상담
법인세법 기반 AI 상담 서비스

---
""")
    st.markdown("""
<div class="ctb-sidebar-guide">
<p><strong>안내사항</strong></p>
<p>본 시스템은 법인세법(2026. 1. 2. 시행)을 기반으로 답변을 제공합니다.</p>
<ul>
<li>조문 기반 정확한 답변</li>
<li>최신 개정 법령 반영</li>
<li>전문 세무 용어 지원</li>
</ul>
</div>
""", unsafe_allow_html=True)
    st.markdown("---")

    if st.button("🗑️ 대화 초기화", use_container_width=True):
        st.session_state.message_list = []
        st.rerun()

    st.markdown("---")
    st.markdown("""
<div style="font-size:0.78rem; color:#7A90B0; line-height:1.7;">
📌 본 답변은 참고용이며<br>
법적 효력을 갖지 않습니다.<br>
정확한 판단은 담당 세무사와<br>
상담하시기 바랍니다.
</div>
""", unsafe_allow_html=True)

# ── 헤더 + 배지 (하나의 카드로 연결) ─────────────────
st.markdown("""
<div class="ctb-header-card">
    <div class="ctb-header-top">
        <div class="ctb-header-icon">⚖️</div>
        <div>
            <p class="ctb-header-title">법인세 AI 상담 시스템</p>
            <p class="ctb-header-subtitle">법인세법 조문을 기반으로 정확하고 신뢰할 수 있는 답변을 드립니다</p>
        </div>
    </div>
    <hr class="ctb-header-divider">
    <div class="ctb-badge-row">
        <span class="ctb-badge">📋 법인세법 2026 최신</span>
        <span class="ctb-badge">🔍 RAG 기반 검색</span>
        <span class="ctb-badge">🤖 AI 자동 답변</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── 본문 안내 카드 (헤더와 연결된 하단 카드) ──────────
st.markdown("""
<div class="ctb-body-card">
    <p class="ctb-guide-text">
        법인세와 관련된 궁금한 사항을 아래 입력창에 질문해 주세요.<br>
        법인세법 조문을 검토하여 관련 조항과 함께 답변드립니다.
    </p>
</div>
""", unsafe_allow_html=True)

# ── 예시 질문 아코디언 ────────────────────────────────
with st.expander("💡 이런 질문을 해보세요", expanded=False):
    st.markdown("""
<div class="ctb-examples-text">
▸ 법인세 과세표준 계산 시 손금불산입 항목에는 어떤 것들이 있나요?<br>
▸ 접대비 한도액은 어떻게 계산하나요? 관련 조문을 알려주세요.<br>
▸ 결손금 소급공제 신청 요건과 절차가 궁금합니다.<br>
▸ 감가상각비 시부인 계산 방법을 설명해 주세요.
</div>
""", unsafe_allow_html=True)

# ── 세션 초기화 ───────────────────────────────────────
if 'message_list' not in st.session_state:
    st.session_state.message_list = []

# ── 이전 대화 누적 표시 (원본 로직 유지) ──────────────
for message in st.session_state.message_list:
    with st.chat_message(message['role']):
        st.write(message['content'])

# ── 채팅 입력창 ──────────────────────────────────────
if userQuestion := st.chat_input(placeholder="법인세에 관련된 궁금한 내용을 말씀해 주세요."):
    with st.chat_message("user"):
        st.write(userQuestion)
    st.session_state.message_list.append({'role': 'user', 'content': userQuestion})
    with st.spinner("법인세법 조문을 검토하여 답변을 생성하는 중입니다..."):
        ai_response = get_ai_response(userQuestion)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
        st.session_state.message_list.append({'role': 'ai', 'content': ai_message})

# ── 푸터 ─────────────────────────────────────────────
st.markdown("""
<div class="ctb-footer">
    법인세 AI 상담 시스템 &nbsp;·&nbsp; 법인세법 기준 (시행 2026. 1. 2.)<br>
    본 답변은 참고용이며 법적 효력을 갖지 않습니다
</div>
""", unsafe_allow_html=True)
