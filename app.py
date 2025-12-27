import streamlit as st
import google.generativeai as genai

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Exam_Viva", page_icon="🎓")

# --- 🔑 SETUP API KEY (SECURE) ---
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("Missing API Key. Please add it to .streamlit/secrets.toml")
    
    # Configure the model
    model = genai.GenerativeModel('models/gemini-flash-latest') 
    
except Exception as e:
    st.error(f"Error configuring API Key: {e}")

# --- APP HEADER ---
st.title("🎓 Exam_Viva")
st.subheader("Your Personal Viva Examiner")
st.markdown("Paste your chapter/notes below. The AI will generate questions with **hidden answers**.")

# Input Box
user_text = st.text_area("Paste text here:", height=150)

# --- THE LOGIC ---
if st.button("Generate Viva Questions", type="primary"):
    if not user_text:
        st.warning("⚠️ Please paste some text first!")
    else:
        with st.spinner("Professor is preparing the quiz..."):
            try:
                # --- UPDATED PROMPT FOR HIDDEN ANSWERS ---
                prompt = f"""
                Act as a strict university examiner. 
                Read the following text: "{user_text}"
                
                Create 5 conceptual viva questions based on this text.
                
                CRITICAL FORMATTING INSTRUCTIONS:
                You must format the output using HTML <details> tags to hide the answers.
                Follow this exact structure for every question:

                **Q1:** [Write the Question Here]
                <details>
                <summary>👇 Click to Reveal Answer</summary>
                [Write the Answer Here]
                </details>
                
                (Repeat for 5 questions)
                """
                
                # Get response
                response = model.generate_content(prompt)
                
                # --- UPDATED DISPLAY LOGIC ---
                st.markdown("### 📝 Your Practice Questions")
                st.markdown(response.text, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.caption("Built for GenAI Hackathon Delhi")