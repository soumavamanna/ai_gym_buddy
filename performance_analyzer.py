import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Generating Synthetic Data
def get_weekly_metrics():
    # Structuring data around a 6-day Push/Pull/Legs regimen
    days = ['Mon (Push)', 'Tue (Pull)', 'Wed (Legs)', 'Thu (Push)', 'Fri (Pull)', 'Sat (Legs)', 'Sun (Rest)']
    
    data = {
        'Day': days,
        'Overall_Score': [88, 92, 84, 91, 89, 82, 0],
        'Form_Accuracy': [94, 91, 83, 95, 90, 80, 0], # Drop in accuracy on heavy leg days
        'Volume_Reps': [140, 135, 110, 145, 130, 105, 0]
    }
    return pd.DataFrame(data)

@st.cache_data
def get_weight_progression():
    # Simulating a steady hypertrophy phase starting from baseline
    weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
    weight = [62.0, 62.3, 62.5, 62.8] 
    return pd.DataFrame({'Week': weeks, 'Body Weight (kg)': weight})


def render_performance_tab():
    st.markdown("### 📈 Pose-to-Performance Analyzer")
    st.write("Review your weekly motion efficiency, workout volume, and hypertrophy progress.")
    
    df_weekly = get_weekly_metrics()
    df_weight = get_weight_progression()
    
    # Top Level Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Avg Form Accuracy", "88.8%", "1.2%")
    with col2:
        st.metric("Total Weekly Reps", "765", "45 reps")
    with col3:
        st.metric("Current Weight", "62.8 kg", "0.8 kg")

    st.divider()

    # Layout for Charts
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.markdown("#### Form Accuracy vs. Overall Score")
        # Filtering out the rest day for cleaner graphing
        active_days = df_weekly[df_weekly['Day'] != 'Sun (Rest)']
        
        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(x=active_days['Day'], y=active_days['Overall_Score'], name='Overall Score', marker_color='#4C78A8'))
        fig_bar.add_trace(go.Bar(x=active_days['Day'], y=active_days['Form_Accuracy'], name='Form Accuracy (%)', marker_color='#F58518'))
        fig_bar.update_layout(barmode='group', height=400, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig_bar, use_container_width=True)

    with chart_col2:
        st.markdown("#### Hypertrophy Progression")
        fig_line = px.line(df_weight, x='Week', y='Body Weight (kg)', markers=True)
        fig_line.update_traces(line_color='#E45756', line_width=3, marker=dict(size=10))
        fig_line.update_layout(height=400, margin=dict(l=0, r=0, t=30, b=0))
        # Set y-axis to tightly frame the data for better visualization
        fig_line.update_yaxes(range=[61.5, 63.5])
        st.plotly_chart(fig_line, use_container_width=True)
        
    st.markdown("#### Training Volume Analysis")
    fig_area = px.area(active_days, x='Day', y='Volume_Reps', color_discrete_sequence=['#72B7B2'])
    fig_area.update_layout(height=300, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig_area, use_container_width=True)