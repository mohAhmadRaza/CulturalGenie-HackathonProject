import streamlit as st
from groq import Groq
import os

# Initialize Groq client using your API key (set in your environment variables)
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


# Function to call Groq API for translation and cultural insights
def call_groq_api(prompt, language):
    try:
        # Make the Groq API call with the prompt and language
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Translate the following text to {language} and provide cultural insights: {prompt}"
                }
            ],
            model="llama3-8b-8192",  # Specify the model
        )

        # Extract the response from Groq
        translation_and_insight = chat_completion.choices[0].message.content
        return {
            'translation': translation_and_insight,
        }

    except Exception as e:
        return {
            'translation': "Error in translation.",
        }


# Function to provide etiquette tips based on region
def get_etiquette_tips(country):
    try:
        # Make the Groq API call with the prompt and language
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Provide detailed cultural etiquette tips for {country}. Include information on greetings, dining etiquette, and business norms. Focus on common practices, important gestures, and any taboos or behaviors that should be avoided in that culture."
                }
            ],
            model="llama3-8b-8192",  # Specify the model
        )

        # Extract the response from Groq
        tips = chat_completion.choices[0].message.content
        return {
            'tips': tips,
        }

    except Exception as e:
        return {
            'translation': "Error in Generating tips.",
        }


# UI Styling and Layout
def build_ui():
    st.set_page_config(
        page_title="Culture Genie",
        page_icon="🌍",
        layout="centered"
    )

    # Custom CSS for UI Styling
    st.markdown("""
    <style>
        .main {
            background-color: #f4f7fc;
        }
        .block-container {
            padding-top: 2rem;
        }
        h1 {
            color: #00aaff;
            font-size: 3rem;
        }
        footer {
            visibility: hidden;
        }
        .stTextInput > div > input {
            background-color: #fff3e6;
        }
        button {
            background-color: #ff4500 !important;
            color: white !important;
            border-radius: 10px !important;
        }
        .reportview-container {
            flex-direction: column;
            align-items: center;
            padding-top: 4rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("🌍 Culture Genie")
    st.subheader("Understand, Translate, and Adapt Across Cultures")

    # Input Box for User Text
    user_input = st.text_input("Enter the text about which you want to learn Cultural Insights:")

    # Language Selection Dropdown
    target_language = st.selectbox("Select target language:", ["Spanish", "French", "Japanese", "German"])
    country = st.selectbox("Select Country For Tips:", ["Japan", "Pakistan", "USA", "German", "India", "Egypt", "France", "UAE", "Turkey"])

    # Generate Insights Button
    if st.button("Generate Insights"):
        if user_input:
            # Call the Groq API with user input and selected language
            result = call_groq_api(user_input, target_language)
            st.write("### Cultural Insightful Text:")
            st.info(result['translation'])
            tips = get_etiquette_tips(country)
            st.write("### Cultural Insightful Text:")
            st.info(tips['tips'])
        else:
            st.warning("Please enter some text to generate insights!")

    # Footer
    st.markdown("---")
    st.markdown("Powered by **Ahmad Raza** via **AI models**")


# Main function to run the app
if __name__ == "__main__":
    build_ui()
