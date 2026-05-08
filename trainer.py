import cv2
import mediapipe as mp
import numpy as np
import streamlit as st

def calculate_angle(a, b, c):
    """Calculates the angle between three points."""
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    if angle > 180.0: 
        angle = 360 - angle
    return angle

def render_trainer_tab():
    """Renders the UI and logic for the AI Vision Trainer."""
    st.markdown("### Bicep Curl Tracker")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        run = st.checkbox('Turn On Webcam')
        FRAME_WINDOW = st.image([])
        
    with col2:
        st.markdown("### 📊 Live Stats")
        metric_placeholder = st.empty()
        if st.button("Reset Counter"):
            st.session_state.counter = 0
            st.session_state.stage = None

    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    if run:
        cap = cv2.VideoCapture(0)
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while run:
                ret, frame = cap.read()
                if not ret: break
                
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = pose.process(image)
                image.flags.writeable = True
                
                try:
                    landmarks = results.pose_landmarks.landmark
                    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                    wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                    
                    angle = calculate_angle(shoulder, elbow, wrist)
                    
                    if angle > 160: st.session_state.stage = "down"
                    if angle < 30 and st.session_state.stage == 'down':
                        st.session_state.stage = "up"
                        st.session_state.counter += 1
                    
                    cv2.putText(image, str(int(angle)), tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                except Exception:
                    pass
                
                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                
                FRAME_WINDOW.image(image)
                metric_placeholder.metric(label="Repetitions", value=st.session_state.counter, delta=st.session_state.stage)
        cap.release()