import time, os, emoji
import streamlit as st
from datetime import datetime
from datetime import timezone
from datetime import timedelta
from sayagain.service.llm import sayagin_kimi

tz = timezone(
    timedelta(hours=8),
    name='Asia/Shanghai',
)

colors = ['blue', 'green', 'orange', 'red', 'violet', 'gray', 'rainbow']
emojis = ['🧸', '🎊', '🎉', '🎎', '🪭', '🏮', '🏮']

page_icon = "🧸"
page_title = "Say it again"


answer = """
Enter api_key to start.
"""

img_url = "https://source.unsplash.com/1600x900/?background"
img_ref = "https://unsplash.com/"

st.set_page_config(
    page_title=page_title, 
    page_icon=page_icon, 
)
# sidebar()

instructions = st.selectbox(
    "语气风格?",
    ("阴阳怪气", "喵娘", "更专业", "温柔", "正式", "非正式")
)

# style = open('moment/style.css').read()

st.markdown(f"""
<style>

</style>""",unsafe_allow_html=True)

input = st.text_input("Say something")


if input:
    # messages = st.container(height=500)
    # messages.chat_message("user").write(input)
    resp = sayagin_kimi(input, instructions)
    st.info(resp, icon="🧸")
    # messages.chat_message("assistant").write(f"{resp}")