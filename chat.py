import streamlit as st

from dotenv import load_dotenv

from llm import get_ai_response

# 환경변수를 불러옴
load_dotenv()

st.set_page_config(page_title='소득세 쳇봇', page_icon='✈️')

st.title('✈️소득세 챗봇')
st.caption('소득세에 관련된 모든것을 답해드립니다.!')

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    with st.chat_message(message['role']):
        st.write(message['content'])




if userQuestion := st.chat_input(placeholder='소득세에 관련된 궁금한 내용을 말씀해 주세요.'):
    with st.chat_message("user"):
        st.write(userQuestion)
    st.session_state.message_list.append({'role':'user', 'content':userQuestion})
    with st.spinner('답변을 생성하는 중입니다.'):
        ai_response = get_ai_response(userQuestion)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)        
        st.session_state.message_list.append({'role':'ai', 'content':ai_message})