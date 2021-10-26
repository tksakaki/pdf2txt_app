#!/Users/tksakaki/.pyenv/versions/3.6.4/bin/python3.6
"""A command line tool for extracting text and images from PDF and
output it to plain text, html, xml or tags."""

import pdfminer.high_level
import streamlit as st





title = '英語論文からDEEPLに入力する英文を抽出するやつ'
st.set_page_config(page_title=title, layout = 'centered', initial_sidebar_state = 'auto')
st.title(title)


uploaded_file=st.file_uploader("論文ファイル", type='pdf')
if(uploaded_file):
    #pdfminer.high_level.extract_text_to_fp(fp, **locals())
    text = pdfminer.high_level.extract_text(uploaded_file)
    text = text.replace("\n\n","[ENTER]")
    text = text.replace("\n","")
    text = text.replace("[ENTER]","\n\n")
    st.code(text)
    
