import streamlit as st
import random

import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyCUiK-jsVHyHK7IEhBYi_bAbi9njoDM8-I')

st.title('')


def expensive_computation():
        # Imagine a time-consuming computation here
        
        questions = [
            "Why is it important to play outside and stay active every day?",
            "How does running or playing sports help your heart stay healthy?",
            "Why is stretching important before and after exercising?",
            "What can you do if you feel too tired to play or exercise?",
            "Why should you try different kinds of sports and activities?",
            "How can you stay active even when the weather is bad outside?",
            "What are the benefits of playing team sports with friends?",
            "Why should you take breaks from sitting for long periods of time?"
        ]
        # question = ''
        
        choice = random.randint(0,7)
        
        question = questions[choice]
        
        st.title(question)
        
        return question
if st.button('next question'):
        question = expensive_computation()

a = st.chat_input('enter your answer here')

if a:
    persauna = 'you are an ai which check the answer given by the user the question will be provided to you and you have to tell if it is carrect or incorrect and why and what will be the coeerct answer if incorrect and also mention the question the question is :'
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(persauna+question+'the answer is :'+a)
    st.write(response.text)
