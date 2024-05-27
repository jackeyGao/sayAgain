import time, os, emoji
import streamlit as st
from datetime import datetime
from datetime import timezone
from datetime import timedelta
from sayagain.service.llm import sayagain

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

# style = open('moment/style.css').read()

st.markdown(f"""
<style>

</style>""",unsafe_allow_html=True)

instructions = st.selectbox(
    "语气风格?",
    ("阴阳怪气", "喵娘", "更专业")
)

messages = st.container(height=300)


if input := st.chat_input("Say something"):
    messages.chat_message("user").write(input)
    resp = sayagain(input, instructions)
    messages.chat_message("assistant").write(f"{resp.content}")