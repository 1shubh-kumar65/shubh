import streamlit as st
import random

import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyCUiK-jsVHyHK7IEhBYi_bAbi9njoDM8-I')

st.title('')

@st.cache_data
def expensive_computation():
        # Imagine a time-consuming computation here
        
        questions = [
            'Which yoga asana depicts an acute angle ?',
                'which state has the highest health index in india'
        ]
        # question = ''
        
        choice = 1
        
        question = questions[choice]
        
        st.title(question)
        
        return question

question = expensive_computation()

a = st.chat_input('enter your answer here')

if a:
    persauna = 'you are an ai which check the answer given by the user the question will be provided to you and you have to tell if it is carrect or incorrect and why and what will be the coeerct answer if incorrect and also mention the question some data is kerela has the highest health index in india the question is :'
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(persauna+question+'the answer is :'+a)
    st.write(response.text)
