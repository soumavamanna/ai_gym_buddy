import streamlit as st

def render_dietician_tab(model):
    """Renders a pure, fast Chatbot UI without RAG complexity."""
    st.markdown("### 💬 Your Personal Nutrition & Motivation Coach")
    
    # Initializing chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
        
    # Rendering existing messages
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_prompt := st.chat_input("Ask about your diet, macros, or next workout..."):
        
        with st.chat_message("user"):
            st.markdown(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})
        
        with st.chat_message("assistant"):
            # Building chat history for Gemini
            formatted_history = [
                {"role": "user", "parts": [m["content"]]} if m["role"] == "user" 
                else {"role": "model", "parts": [m["content"]]} 
                for m in st.session_state.chat_history[:-1]
            ]
            
            # Sending to Gemini
            chat = model.start_chat(history=formatted_history)
            response = chat.send_message(user_prompt)
            st.markdown(response.text)
            
        st.session_state.chat_history.append({"role": "assistant", "content": response.text})