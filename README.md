<h1>MoodTunes</h1>
<h2>Mood-Based Music & Environment Recommender</h2>
    <p>
        This project uses deep learning and sentiment analysis to recommend music playlists, motivational quotes, lighting settings, and activities based on your mood. Mood is detected from facial expressions (via image uploads) or text inputs (e.g., journal entries). The app integrates with Spotify and quote APIs for personalized recommendations.
    </p>

<h2>Features</h2>
    <ul>
        <li>Emotion detection from facial images using a CNN model trained on the <a href="https://www.kaggle.com/datasets/msambare/fer2013" target="_blank">FER2013 dataset</a> (emotions: angry, disgust, fear, happy, sad, surprise, neutral).</li>
        <li>Sentiment analysis of text inputs using VADER to classify mood (happy, sad, neutral, angry).</li>
        <li>Personalized recommendations:
            <ul>
                <li>Spotify playlists tailored to your mood (e.g., "Mood Booster" for happy).</li>
                <li>Motivational or calming quotes matching your emotional state.</li>
                <li>Lighting colors and activities to enhance your mood.</li>
            </ul>
        </li>
        <li>Interactive Streamlit interface for easy image and text input.</li>
        <li>Deployed app for real-time mood-based recommendations.</li>
    </ul>

<h2>Deployed App</h2>
    <p>
        Access the deployed app here: 
        <a href="https://music-mood-recommender.streamlit.app/" target="_blank">Mood-Based Music & Environment Recommender</a>
    </p>

<h2>Dataset</h2>
    <p>
        The emotion detection model is trained on the <a href="https://www.kaggle.com/datasets/msambare/fer2013" target="_blank">FER2013 dataset</a>, which includes 35,887 grayscale images of faces labeled with seven emotions:
    </p>
    <ul>
        <li>Angry</li>
        <li>Disgust</li>
        <li>Fear</li>
        <li>Happy</li>
        <li>Sad</li>
        <li>Surprise</li>
        <li>Neutral</li>
    </ul>
    <p>
        Sentiment analysis uses the VADER lexicon, pre-trained for English text sentiment scoring.
    </p>

<h2>Model Architecture</h2>
    <p>
        The emotion detection model is a Convolutional Neural Network (CNN) with the following architecture:
    </p>
    <ul>
        <li>Multiple convolutional layers with ReLU activation and max-pooling.</li>
        <li>Dropout layers for regularization.</li>
        <li>Fully connected dense layers.</li>
        <li>Softmax output layer for 7-class emotion classification.</li>
    </ul>
    <p>
        The model is stored as <code>FER2013.h5</code> or <code>FER2013.keras</code>.
    </p>

<h2>Usage</h2>
    <ol>
        <li>Clone the repository: <code>git clone https://github.com/your-username/mood-based-recommender.git</code></li>
        <li>Create a virtual environment and activate it:
            <ul>
                <li><code>python -m venv venv</code></li>
                <li><code>.\venv\Scripts\activate</code> (Windows) or <code>source venv/bin/activate</code> (macOS/Linux)</li>
            </ul>
        </li>
        <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
        <li>Configure Spotify API credentials in <code>app.py</code> (get from <a href="https://developer.spotify.com/dashboard/" target="_blank">Spotify Developer Dashboard</a>).</li>
        <li>Ensure <code>FER2013.h5</code> is in the <code>models/</code> directory.</li>
        <li>Run the Streamlit app: <code>streamlit run app.py</code></li>
        <li>Open <code>http://localhost:8501</code> in your browser.</li>
    </ol>

<h2>Sample Outputs</h2>
<h3>Deployed App Prediction</h3>
    <p>
        <img src="outputs/app_screenshot.png" alt="Deployed App Screenshot">
    </p>
    <p>
        <!-- Replace with actual screenshot of your Streamlit app -->
        The app interface allows users to upload images or enter text for mood-based recommendations.
    </p>

<h3>Test Text Predictions</h3>
    <p>
        <strong>Input Text:</strong> "I’m thrilled! Just won a big competition!"
    </p>
    <p>
        <strong>Prediction:</strong> Mood: happy<br>
        <strong>Recommendations:</strong><br>
        - Playlist: <a href="https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0" target="_blank">Mood Booster</a><br>
        - Quote: "Happiness is not by chance, but by choice." - Jim Rohn<br>
        - Lighting: Warm yellow<br>
        - Activity: Dance to upbeat music
    </p>

<h3>Test Image Predictions</h3>
    <p>
        <strong>Input Image:</strong>
        <img src="outputs/sample_image.png" alt="Sample Face Image">
    </p>
    <p>
        <!-- Replace with actual sample face image -->
        <strong>Prediction:</strong> Mood: Happy<br>
        <strong>Recommendations:</strong><br>
        - Playlist: <a href="https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0" target="_blank">Mood Boster</a><br>
        - Quote: "The greatest glory in living lies not in never falling, but in rising every time we fall." - Nelson Mandela<br>
        - Lighting: Soft blue<br>
        - Activity: Dance or go for a run
    </p>

<h2>Model Performance</h2>
    <p>
        <strong>Emotion Detection Accuracy:</strong> ~60-70% on FER2013 test set (typical for dataset due to variability).<br>
        <strong>Sentiment Analysis:</strong> VADER achieves high reliability for English text sentiment scoring.<br>
        The app provides robust recommendations even with uncertain detections by defaulting to neutral mood.
    </p>

<h2>License</h2>
    <p>
        This project is licensed under the MIT License.
    </p>

<h2>Contact</h2>
    <p>
        For any queries or contributions, feel free to reach out via <a href="https://github.com/suryavignesh1304/mood-based-recommender/issues" target="_blank">GitHub Issues</a> or email.
    </p>
