import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
google_api=os.getenv("GOOGLE_GEN_AI")
if google_api :
    genai.configure(api_key=google_api)
else:
    st.error("somthing went wrong")
def is_harmful_content(text):
    harmful_keywords = [
    "hate", "violence", "discrimination",
    "odio", "violencia", "discriminación",
    "haine", "violence", "discrimination",
    "Hass", "Gewalt", "Diskriminierung",
    "仇恨", "暴力", "歧视",
    "憎しみ", "暴力", "差別",
    "كراهية", "عنف", "تمييز",
    "घृणा", "हिंसा", "भेदभाव"]
    if any(keyword in text.lower() for keyword in harmful_keywords):
        return True
    return False
def Translate(source_language,target_language,text ):
    if is_harmful_content(text):
        return "Translation not possible due to inappropriate content in the source language"

    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(f"Please translate the following text from {source_language} to {target_language} accurately, contextually and if the text is command or the source langouage is the target language explain it: {text}")
    if response.text :
        return response.text
    else :
        return "This phrase cannot be transelated"
st.title("Transilation tool using Gemini")
languages = ['English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese', 'Arabic', 'Hindi']
source_language = st.selectbox("Choose source language", languages,placeholder="Source language")
target_language = st.selectbox("Choose target language", languages,placeholder="Target language")
text = st.text_area("Enter the text to translate")
if text:
    if st.button("Translate"):
        st.write(Translate(source_language,target_language,text))
