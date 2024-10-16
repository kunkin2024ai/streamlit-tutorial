## llama_streamlit_app.py
## 아래는 LM Studio에서 LLAMA3.2 기반 앱을 실행하는 영상과 소스코드입니다 :
## 

import streamlit as st
from openai import OpenAI

# OpenAI 클라이언트 설정
@st.cache_resource
def get_openai_client():
    return OpenAI(base_url="http://<Your IP>:5555/v1", api_key="lm-studio")

client = get_openai_client()

st.title("LM Studio 채팅 앱")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are helpful instance."}
    ]

# 채팅 메시지를 표시할 컨테이너
chat_container = st.container()

# 입력 필드를 화면 하단에 고정
input_container = st.container()

# 대화 내용 표시
with chat_container:
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.write(message["content"])

# 사용자 입력 (화면 하단에 위치)
with input_container:
    user_input = st.text_input("메시지를 입력하세요:", key="user_input")
    send_button = st.button("전송")

if send_button and user_input:
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with chat_container:
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # 스트리밍 응답
            for response in client.chat.completions.create(
                model="lmstudio-community/Llama-3.2-3B-Instruct-GGUF",
                messages=st.session_state.messages,
                temperature=0.7,
                stream=True
            ):
                full_response += (response.choices[0].delta.content or "")
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
    
    # 최종 응답 메시지 추가
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    # 입력 필드 초기화 (st.session_state 사용하지 않음)
    st.rerun()

# 스크롤을 항상 최하단으로 이동
st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)
