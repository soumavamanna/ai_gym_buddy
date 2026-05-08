import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Generating Synthetic Training Data
@st.cache_data
def load_and_train_model():
    """Generates dummy data and trains the prediction model."""
    np.random.seed(42)
    
    # Simulating 100 days of a 6-Day PPL split
    data = {
        'Sleep_Hours': np.random.uniform(4.0, 9.0, 100),
        'Calories_Logged': np.random.randint(1800, 3500, 100),
        'Day_of_Week': np.random.randint(0, 7, 100), # 0=Monday, 6=Sunday
        'Muscle_Soreness_1to10': np.random.randint(1, 10, 100),
    }
    df = pd.DataFrame(data)
    
    # Logic for generating the target variable (Will_Skip: 1=Yes, 0=No)
    # E.g., High soreness, low sleep, or Sunday (Rest Day) increases skip chance
    skip_condition = (df['Sleep_Hours'] < 6) | (df['Muscle_Soreness_1to10'] > 7) | (df['Day_of_Week'] == 6)
    df['Will_Skip'] = np.where(skip_condition, 1, 0)
    
    # Adding some noise to make it realistic
    noise = np.random.choice([0, 1], size=100, p=[0.85, 0.15])
    df['Will_Skip'] = np.where(noise == 1, 1 - df['Will_Skip'], df['Will_Skip'])

    # Training the Model
    X = df.drop('Will_Skip', axis=1)
    y = df['Will_Skip']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    
    return model

def render_habit_tab():
    st.markdown("### 🧠 AI Fitness Habit & Behavior Predictor")
    st.write("This module analyzes your daily metrics to predict the likelihood of skipping today's session, helping you prevent burnout.")
    
    # Load the ML model
    model = load_and_train_model()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Input Today's Metrics")
        sleep = st.slider("Sleep Hours Last Night", 3.0, 10.0, 7.0, 0.5)
        calories = st.number_input("Target Calories for Today", min_value=1500, max_value=4000, value=2800, step=100)
        day_of_week = st.selectbox("Day of the Week", [0, 1, 2, 3, 4, 5, 6], format_func=lambda x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][x])
        soreness = st.slider("Muscle Soreness (1 = Fresh, 10 = Exhausted)", 1, 10, 3)
        
        predict_btn = st.button("Predict Workout Probability")

    with col2:
        st.markdown("#### AI Prediction Insight")
        if predict_btn:
            # Format input for the model
            input_data = pd.DataFrame({
                'Sleep_Hours': [sleep],
                'Calories_Logged': [calories],
                'Day_of_Week': [day_of_week],
                'Muscle_Soreness_1to10': [soreness]
            })
            
            # Get prediction and probability
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1] * 100 # Probability of skipping
            
            if prediction == 1:
                st.error(f"🚨 **High Risk of Skipping!** ({probability:.1f}% probability)")
                st.write("**AI Nudge:** Your metrics indicate fatigue. If you are doing your Leg Day today, consider switching to a lighter active recovery day or prioritizing sleep tonight.")
            else:
                st.success(f"✅ **You are on track!** (Only {probability:.1f}% risk of skipping)")
                st.write("**AI Nudge:** Conditions are optimal. Stick to your Push/Pull/Legs protocol and crush it!")