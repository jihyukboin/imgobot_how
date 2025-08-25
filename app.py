import streamlit as st

from pathlib import Path

APP_ROOT = Path(__file__).parent

def resolve_src(src: str) -> str:
    """URL이면 그대로, 로컬이면 백슬래시→슬래시 변환 후 앱 루트 기준 절대경로로 변환."""
    if isinstance(src, str) and src.startswith(("http://", "https://")):
        return src
    # 백슬래시를 슬래시로 바꾸고, 앱 루트 기준으로 합치기
    p = (APP_ROOT / src.replace("\\", "/")).resolve()
    return str(p)
# ---------------------------------------------
# 기본 설정
# ---------------------------------------------
st.set_page_config(
    page_title="임고봇 사용 설명서",
    page_icon="📘",
    layout="wide",
)

# ---------------------------------------------
# 스타일 커스터마이징 (필요 시 수정)
# ---------------------------------------------
st.markdown(
    """
    <style>
    body, .stApp, .main, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
        background: #fff !important;
    }
    .app-title { font-size: 2rem; font-weight: 800; margin-bottom: .5rem; }
    .app-subtitle { color: #6b7280; margin-bottom: 1.5rem; }
    .block { background: #fff; border-radius: 16px; padding: 18px 20px; box-shadow: 0 2px 10px rgba(0,0,0,.06); }
    .muted { color: #6b7280; }
    .kbd { display:inline-block; padding: 2px 6px; border-radius: 6px; background:#f3f4f6; border:1px solid #e5e7eb; font-size: .9rem; }
    .cap { color:#6b7280; font-size:.9rem; margin-top:.25rem; }
    .mb16 { margin-bottom: 16px; }
    .mb24 { margin-bottom: 24px; }
    .mb32 { margin-bottom: 32px; }
    .mt8 { margin-top: 8px; }
    .mt16 { margin-top: 16px; }
    .hr { height:1px; background:#e5e7eb; margin: 24px 0; }

    /* 추가: 비디오/이미지 + 텍스트를 하나로 묶는 컨테이너 */
    .group { background:#fff; border:2px solid #000; border-radius:16px; padding:18px 20px; }
    .group .caption { color:#6b7280; font-size:.9rem; margin-top:.25rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------
# 예시 이미지 URL (원하는 이미지/로컬 경로로 교체하세요)
# - 로컬 파일을 쓰려면: "./images/feature1-step1.png" 형태로 바꿔주세요
# ---------------------------------------------
IMG = {
    "f1_1": "asset\\image\\my_sz\\my_sz_main1.png",

}

MEDIA = {
    "M1_1": "asset\\image\\my_sz\\Video\\mz_sz\\sz_2mp4.mp4",
    "M1_2": "asset\\image\\my_sz\\Video\\mz_sz\\sz_2.mp4",
    "M1_3": "asset\\image\\my_sz\\Video\\mz_sz\\sz_3.mp4",
    "M1_4": "asset\\image\\my_sz\\Video\\mz_sz\\sz_4.mp4",
    "M1_5": "asset\\image\\my_sz\\Video\\mz_sz\\sz_5.mp4",
    
}

# ---------------------------------------------
# 기능별 콘텐츠 정의
# - 순서: 사진 -> 텍스트 -> 사진 -> 텍스트
# - 아래 본문을 실제 서비스에 맞게 자유롭게 수정하세요.
# ---------------------------------------------
FEATURES = {
    "마이스제트": [

        {
            "type": "text",
            "title": "마이스제트 기능은 무엇인가요?",
            "body": (
                "마이스제트 기능은 기존 스제트를 임고봇 안에서 보다 편리하고 효율적으로 활용할 수 있게 만든 기능입니다.\n\n"
                "- 고유하게 할당된 나만의 저장 공간에서 자유롭게 스제트를 작성할 수 있습니다.\n"
                "- 기존 1차 퀴즈 유사도채점 방식을 도입하여 보다 확실하게 공부할 수 있습니다.\n"
                "- 찾고자하는 텍스트가 어떤 과목 , 어떤 컨테이너, 어떤 행에 있더라도 [통합검색] 기능을 통해 간편하게 검색하고, 해당 컨텐츠로 이동할 수 있습니다."
            )
        },

 ##-------------------------------------------------------------------------------------------------------------
        {
            "type": "image",
            "src": IMG["f1_1"],
            "caption": "마이스제트 페이지"
        },


        {
            "type": "text",
            "title": "사용 방법-과목,컨테이너,행.",
            "body": (
                "1) 좌측 사이드탭에서 과목을 클릭합니다.(이때 , 과목을 마우스로 드래그하여 순서를 변경할 수 있습니다.)\n\n"
                
                "2) 클릭한 과목의 컨테이너와 컨테이너의 행들이 나타납니다."
                

            )
        },

 ##-------------------------------------------------------------------------------------------------------------


 ##-------------------------------------------------------------------------------------------------------------
        {
            "type": "video",
            "src": MEDIA["M1_1"],
            "caption": "행 추가 방법"
        },
        {
            "type": "text",
            "title": "사용 방법-행 추가하기.",
            "body": (
                "1) 상단에 위치한 3모드 토글을 클릭해 [EDIT] 모드로 변경합니다.\n\n"
                "2) 문제 텍스트와 정답 텍스트를 입력한 후 컨테이너 우측 상단에 위치한 [저장] 아이콘을 클릭합니다.\n\n"
                "3) 기본적으로 자동저장 기능이 지원됩니다. 만약 저장버튼을 누를 필요가 없는 경우 , 초록색 체크 아이콘이 나타납니다."
                

                
                

            )
        },


##-------------------------------------------------------------------------------------------------------------

##-------------------------------------------------------------------------------------------------------------
        {
            "type": "video",
            "src": MEDIA["M1_2"],
            "caption": "행,컨테이너 삭제 방법"
        },


        {
            "type": "text",
            "title": "사용 방법-컨테이너와 행 삭제하기.",
            "body": (
                "1) [EDIT]모드가 토글되어 있는 상태에서 각각의 행,컨테이너 우측에 위치한 휴지통 아이콘을 통해 삭제할 수 있습니다. \n\n"
                "2) 행의 경우 5초동안 되돌리기 버튼이 제공되니 실수로 삭제했더라도 걱정하지 마세요. \n\n"
               
                

            )
        },

 ##-------------------------------------------------------------------------------------------------------------

##-------------------------------------------------------------------------------------------------------------
        {
            "type": "video",
            "src": MEDIA["M1_3"],
            "caption": "[VIEW] 모드"
        },


        {
            "type": "text",
            "title": "사용 방법-VIEW 모드.",
            "body": (
                "1) 추가한 컨테이너와 행들의 데이터는 오직 사용자 본인만 열람할 수 있는 안전한 곳에 보관됩니다. \n\n"
                "2) 상단 [VIEW] 모드로 토글하여 추가한 행들과 컨테이너를 열람해보세요."
               
                

            )
        },

 ##-------------------------------------------------------------------------------------------------------------


##-------------------------------------------------------------------------------------------------------------
        {
            "type": "video",
            "src": MEDIA["M1_4"],
            "caption": "[PLAY] 모드"
        },


        {
            "type": "text",
            "title": "사용 방법-PLAY 모드.",
            "body": (
                "1) 상단 [PLAY] 모드로 토글하여 스제트 기능을 활용해보세요.\n\n"
                "2) 문제 풀이가 완료되면 , 다시 [VIEW] 모드로 토글하여 내가 적은 정답들을 비교해보세요."
               
                

            )
        },
##-------------------------------------------------------------------------------------------------------------

##-------------------------------------------------------------------------------------------------------------
        {
            "type": "video",
            "src": MEDIA["M1_5"],
            "caption": "통합 검색 기능"
        },


        {
            "type": "text",
            "title": "사용 방법-통합검색 기능.",
            "body": (
                "1) 좌측 상단에 위치한 통합 검색 기능으로 무엇이든 검색해보세요.\n\n"
                "2) 어떤 과목, 어떤 컨테이너, 어떤 행에 입력했더라도 입력한 텍스트와 관련된 모든 것들을 검색해드립니다.\n\n"
                "3) 추가로 검색 결과를 클릭하여 , 해당 검색결과가 존재하는 곳으로 바로 이동할 수도 있습니다."
                

            )
        },

 ##-------------------------------------------------------------------------------------------------------------


    ]

}

# ---------------------------------------------
# 사이드바: 기능 선택
# ---------------------------------------------
with st.sidebar:
    st.header("📑 목차")
    selected = st.radio("기능 선택", list(FEATURES.keys()), index=0, label_visibility="collapsed")
    st.markdown("---")
    

# ---------------------------------------------
# 본문 렌더링
# ---------------------------------------------
st.markdown("<div class='app-title'>임고봇 사용 설명서</div>", unsafe_allow_html=True)
st.markdown("<div class='app-subtitle'>목차에서 궁금했던 기능을 클릭해보세요.</div>", unsafe_allow_html=True)


content = FEATURES[selected]

# --- 변경: image/video + 다음 text를 하나의 .group 테두리에 묶어 렌더링 ---
i = 0
while i < len(content):
    block = content[i]

    # case 1) media(image/video) + 다음 text → 하나의 group
    if block["type"] in ("image", "video"):
        with st.container():
            st.markdown("<div class='group'>", unsafe_allow_html=True)

            # 1-1) 미디어 렌더
            if block["type"] == "image":


                src = resolve_src(block["src"])
                st.image(src, use_container_width=True, caption=block.get("caption", ""))
                
            elif block["type"] == "video":
                with st.container():
                    st.markdown("<div class='block'>", unsafe_allow_html=True)
                    src = resolve_src(block["src"])

                    # URL이든 로컬이든 정규화된 문자열을 그대로 전달
                    st.video(src, start_time=0)

                    if block.get("caption"):
                        st.caption(block["caption"])
                    st.markdown("</div>", unsafe_allow_html=True)

            # 1-2) 다음 블록이 text면 같은 group에 함께 렌더
            if i + 1 < len(content) and content[i + 1]["type"] == "text":
                text_block = content[i + 1]
                if text_block.get("title"):
                    st.subheader(text_block["title"])
                st.markdown(text_block.get("body", ""), unsafe_allow_html=True)
                i += 1  # 텍스트 블록까지 소비

            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

    # case 2) 그 외(단독 text 등) → 기존 block 스타일 유지
    else:
        if block["type"] == "text":
            with st.container():
                st.markdown("<div class='block'>", unsafe_allow_html=True)
                if block.get("title"):
                    st.subheader(block["title"])        
                st.markdown(block.get("body", ""), unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

    i += 1

# ---------------------------------------------
# 도움말/팁
# ---------------------------------------------
with st.expander("💡 이상으로 기능 설명을 마칩니다. 펼쳐서 추가 코멘트를 확인해보세요."):
    st.markdown(
        """
        - **오류 제보**: 오류가 발견되면 , 페이지 좌측 하단 피드백 입력칸 또는 사용자 게시판에 제보해주세요.  
        - **기능 제안**: 마찬가지로 크고 작은 나만의 아이디어를 공유해주세요. 우선순위를 정해 적극 반영하도록 하겠습니다.   
        - **자료 제공**: 공유하고싶은 자료가 있다면 사용자 게시판 / 파일 업로드 기능을 통해 자료를 공유해주세요. 더 발전된 임고봇을 만드는데 도움이 됩니다.
        - **감사합니다**
        """
    )
