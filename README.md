# 🏋️ AI Gym Buddy: Intelligent Fitness Ecosystem

An end-to-end fitness platform combining **Computer Vision**, **Large Language Models (RAG)**, and **Predictive Analytics** to optimize muscle hypertrophy and workout discipline.

---

### 🚀 Core Features

*   **Real-Time Rep Tracking:** Utilizes **MediaPipe** for pose estimation to track exercise form and count repetitions automatically with high precision.
*   **RAG-Powered Nutrition Coach:** A specialized chatbot using **Retrieval-Augmented Generation** to parse training handbooks and provide science-based diet advice tailored to individual caloric needs.
*   **ML Consistency Predictor:** A machine learning model that analyzes historical workout data to predict consistency and nudge users toward their goals.
*   **Performance Dashboard:** Interactive visualizations built with **Plotly** to monitor progress, strength gains, and habit trends.
*   **Smart Recommendations:** A recommendation engine that aligns training targets with local gym facilities and equipment availability.

---

### 🛠️ Tech Stack

**AI & Computer Vision**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MediaPipe](https://img.shields.io/badge/MediaPipe-007f00?style=for-the-badge&logo=google&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

**Backend & Frontend**
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)

---

### 📂 System Architecture

1.  **Input Layer:** Captures video feed for pose detection and user queries for the nutrition coach.
2.  **Processing Layer:** 
    *   **MediaPipe Pose:** Extracts 33 landmarks to calculate joint angles for form validation.
    *   **Vector Database:** Stores embedded training manuals for the RAG pipeline.
3.  **Analytics Layer:** Runs predictive models via Scikit-learn to forecast workout adherence.
4.  **UI Layer:** A seamless Streamlit dashboard providing real-time feedback and historical data analysis.

---

### 🛠️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/[your-username]/ai-gym-buddy.git
    cd ai-gym-buddy
    ```

2.  **Set up Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install DependenciesThis project is a high-level integration of Computer Vision and Generative AI, designed to act as a comprehensive companion for hypertrophy and consistency. It moves beyond simple tracking by using real-time pose detection and Retrieval-Augmented Generation (RAG) to provide professional-grade form analysis and nutritional guidance.

---

# 🏋️ AI Gym Buddy: Intelligent Fitness Ecosystem

An end-to-end fitness platform combining **Computer Vision**, **Large Language Models (RAG)**, and **Predictive Analytics** to optimize muscle hypertrophy and workout discipline.

---

### 🚀 Core Features

*   **Real-Time Rep Tracking:** Utilizes **MediaPipe** for pose estimation to track exercise form and count repetitions automatically with high precision.
*   **RAG-Powered Nutrition Coach:** A specialized chatbot using **Retrieval-Augmented Generation** to parse training handbooks and provide science-based diet advice tailored to individual caloric needs.
*   **ML Consistency Predictor:** A machine learning model that analyzes historical workout data to predict consistency and nudge users toward their goals.
*   **Performance Dashboard:** Interactive visualizations built with **Plotly** to monitor progress, strength gains, and habit trends.
*   **Smart Recommendations:** A recommendation engine that aligns training targets with local gym facilities and equipment availability.

---

### 🛠️ Tech Stack

**AI & Computer Vision**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MediaPipe](https://img.shields.io/badge/MediaPipe-007f00?style=for-the-badge&logo=google&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

**Backend & Frontend**
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)

---

### 📂 System Architecture

1.  **Input Layer:** Captures video feed for pose detection and user queries for the nutrition coach.
2.  **Processing Layer:** 
    *   **MediaPipe Pose:** Extracts 33 landmarks to calculate joint angles for form validation.
    *   **Vector Database:** Stores embedded training manuals for the RAG pipeline.
3.  **Analytics Layer:** Runs predictive models via Scikit-learn to forecast workout adherence.
4.  **UI Layer:** A seamless Streamlit dashboard providing real-time feedback and historical data analysis.

---
