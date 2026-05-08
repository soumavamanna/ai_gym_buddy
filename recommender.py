import streamlit as st
import pandas as pd

# Mock Database of hometown
@st.cache_data
def load_gym_database():
    """Simulates a database of local gyms and fitness centers."""
    data = {
        'Gym_Name': [
            'Iron Core Fitness', 'Elite Muscle Studio', 'Wellness & Cardio Hub', 
            'Zenith Crossfit', 'Spartan Power Gym', 'Flex & Tone Studio'
        ],
        'City': ['Panskura', 'Kharagpur', 'Kolaghat', 'Panskura', 'Kharagpur', 'Kolaghat'],
        'Specialty': ['Hypertrophy', 'Powerlifting', 'Cardio & Wellness', 'Crossfit', 'Hypertrophy', 'General Fitness'],
        'Rating': [4.8, 4.9, 4.2, 4.5, 4.7, 4.1],
        'Monthly_Fee_INR': [800, 1200, 600, 1000, 900, 500]
    }
    return pd.DataFrame(data)

@st.cache_data
def load_programs():
    """Simulates a database of AI-generated workout programs."""
    return {
        'Hypertrophy': "6-Day Push/Pull/Legs Split (High Volume, 8-12 Reps, focus on progressive overload from 62 kg baseline)",
        'Powerlifting': "4-Day Upper/Lower Split (Low Reps, Heavy Compound Focus, 3-5 Reps)",
        'Cardio & Wellness': "3-Day Full Body Circuit + 2 Days LISS Cardio (Heart Health Focus)",
        'Crossfit': "5-Day WOD (Workout of the Day) including Olympic lifting and high-intensity interval training"
    }

def render_recommender_tab():
    st.markdown("### 📍 Gym & Program Recommender")
    st.write("Find the optimal training facility and automatically align it with a generated workout program.")
    
    gym_df = load_gym_database()
    programs = load_programs()
    
    # --- Input Filters ---
    st.markdown("#### Set Your Parameters")
    col1, col2 = st.columns(2)
    
    with col1:
        # Defaulting to the local area
        selected_city = st.selectbox("Select Location", ["Panskura", "Kharagpur", "Kolaghat"])
    with col2:
        # Defaulting to the known primary fitness goal
        selected_goal = st.selectbox("Primary Fitness Goal", ["Hypertrophy", "Powerlifting", "Cardio & Wellness", "Crossfit"])
        
    st.divider()
    
    st.markdown(f"#### 🏆 Top Recommendations in {selected_city}")
    
    # Filter by city
    local_gyms = gym_df[gym_df['City'] == selected_city]
    
    # Score gyms based on how well they match the goal
    # Exact match gets a boost, otherwise sorted by rating
    local_gyms['Match_Score'] = local_gyms.apply(
        lambda row: row['Rating'] + 1.0 if row['Specialty'] == selected_goal else row['Rating'], axis=1
    )
    recommended_gyms = local_gyms.sort_values(by='Match_Score', ascending=False)
    
    if recommended_gyms.empty:
        st.info("No gyms found in this immediate area. Try expanding your search.")
    else:
        for index, row in recommended_gyms.iterrows():
            with st.expander(f"🏅 {row['Gym_Name']} - Rating: {row['Rating']} ⭐️"):
                st.write(f"**Specialty:** {row['Specialty']}")
                st.write(f"**Estimated Fee:** ₹{row['Monthly_Fee_INR']} / month")
                if row['Specialty'] == selected_goal:
                    st.success("🎯 **Perfect Match** for your current fitness goals!")
                
    st.markdown("#### 📋 Recommended AI Training Protocol")
    st.info(f"**Program Name:** {selected_goal} Protocol\n\n**Overview:** {programs[selected_goal]}")
    
    if st.button("Enroll & Sync to Habit Tracker"):
        st.balloons()
        st.success(f"Successfully enrolled in the {selected_goal} Protocol at {recommended_gyms.iloc[0]['Gym_Name']}! Your Habit Tracker metrics have been updated.")