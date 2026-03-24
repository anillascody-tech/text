import streamlit as st
from google import genai


MODEL_NAME = "gemini-3-flash-preview"
SYSTEM_PROMPT = "你是温柔可爱的 AI 聊天伙伴，回复时自然、友好、简洁。"


st.set_page_config(
    page_title="AI Agent 聊天伙伴",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://docs.streamlit.io/",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": "# 这是一个简单的 AI 聊天程序。",
    },
)

st.title("AI Agent 聊天伙伴")


def init_chat_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []


def render_chat_history() -> None:
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])


def build_total_prompt() -> str:
    lines = [
        SYSTEM_PROMPT,
        "",
        "以下是聊天记录，请结合上下文继续回答最后一条用户消息：",
    ]

    for message in st.session_state.messages:
        speaker = "用户" if message["role"] == "user" else "助手"
        lines.append(f"{speaker}: {message['content']}")

    return "\n".join(lines)


init_chat_state()
render_chat_history()

user_prompt = st.chat_input("和 AI 对话吧")

if user_prompt:
    user_message = {"role": "user", "content": user_prompt}
    st.session_state.messages.append(user_message)
    st.chat_message("user").write(user_prompt)

    client = genai.Client()

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=build_total_prompt(),
        )
        response_text = response.text or "模型没有返回内容。"
    except Exception as exc:
        response_text = f"调用模型失败: {exc}"

    assistant_message = {"role": "assistant", "content": response_text}
    st.session_state.messages.append(assistant_message)
    st.chat_message("assistant").write(response_text)
