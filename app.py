import streamlit as st
import os
from backend.emotion_detection import EmotionDetector
from backend.sentiment_analysis import SentimentAnalyzer
from backend.spotify_integration import SpotifyRecommender
from backend.quote_integration import QuoteGenerator
from backend.recommender import MoodRecommender

# Initialize components
emotion_detector = EmotionDetector()
sentiment_analyzer = SentimentAnalyzer()
spotify_recommender = SpotifyRecommender(
    client_id="0c9afc03fc1145b9818e031c4d790bed",
    client_secret="30268ff8a1ee473886f54d034ffcccda"
)
quote_generator = QuoteGenerator()
recommender = MoodRecommender()

# Streamlit UI
st.title("Mood-Based Music & Environment Recommender")

# Input options
input_type = st.radio("Choose input method:", ("Text", "Image"))

mood = "neutral"
if input_type == "Text":
    text_input = st.text_area("Enter your thoughts (e.g., journal entry):")
    if st.button("Analyze Text"):
        if text_input:
            mood = sentiment_analyzer.analyze_text(text_input)
            st.write(f"Detected mood: **{mood}**")
        else:
            st.error("Please enter some text.")

elif input_type == "Image":
    uploaded_file = st.file_uploader("Upload a facial image:", type=["jpg", "png"])
    if uploaded_file and st.button("Analyze Image"):
        # Save uploaded file temporarily
        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        mood = emotion_detector.detect_emotion("temp_image.jpg")
        st.write(f"Detected mood: **{mood}**")
        os.remove("temp_image.jpg")

# Generate recommendations
if mood != "neutral" or st.button("Get Recommendations"):
    st.subheader("Recommendations")

    # Spotify playlist
    playlist_name, playlist_url = spotify_recommender.get_playlist(mood)
    st.write(f"**Playlist**: [{playlist_name}]({playlist_url})")

    # Lighting and activity
    recs = recommender.generate_recommendations(mood)
    st.write(f"**Lighting**: {recs['lighting']}")
    st.write(f"**Activity**: {recs['activity']}")

    # Quote
    quote, author = quote_generator.get_quote(mood)
    st.write(f"**Quote**: \"{quote}\" — {author}")