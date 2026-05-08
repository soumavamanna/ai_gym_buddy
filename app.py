import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Importing all custom modules
import trainer
import dietician
import habit_tracker
import performance_analyzer
import recommender 


st.set_page_config(page_title="AI Gym Ecosystem", layout="wide")
st.title("⚡ AI Gym & Fitness Assistant")

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("API Key not found! Please check your .env file.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)
system_instruction = """
You are an expert AI Dietician and Fitness Coach specializing in hypertrophy and muscle gain. 
Your primary focus is recommending minimalist, resource-efficient, high-protein Indian diets.
Prioritize ingredients like chicken, eggs, and paneer. 
If calculating macros for the user, assume a baseline target of maintaining or bulking from 62 kg over a 6-day gym split unless specified otherwise.
"""
model = genai.GenerativeModel('gemini-2.5-flash', system_instruction=system_instruction)


if 'counter' not in st.session_state: st.session_state.counter = 0
if 'stage' not in st.session_state: st.session_state.stage = None
if 'chat_history' not in st.session_state: st.session_state.chat_history = []


tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💪 AI Vision Trainer", 
    "🥗 AI Dietician", 
    "🧠 Habit Tracker",
    "📈 Analytics",
    "📍 Recommender" 
]) 

with tab1: trainer.render_trainer_tab()
with tab2: dietician.render_dietician_tab(model)
with tab3: habit_tracker.render_habit_tab()
with tab4: performance_analyzer.render_performance_tab()
with tab5: recommender.render_recommender_tab()