import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import logging

class SentimentAnalyzer:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        try:
            nltk.data.find("sentiment/vader_lexicon")
            self.logger.info("VADER lexicon found.")
        except LookupError:
            self.logger.info("Downloading VADER lexicon...")
            nltk.download("vader_lexicon", quiet=True)
        
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_text(self, text):
        """
        Analyze sentiment of input text.
        Returns 'happy', 'sad', 'neutral', or 'angry' based on compound score.
        """
        try:
            if not isinstance(text, str) or not text.strip():
                self.logger.warning("Invalid or empty text input.")
                return "neutral"
                
            self.logger.info(f"Analyzing text: {text[:50]}...")
            scores = self.analyzer.polarity_scores(text)
            compound = scores["compound"]
            self.logger.info(f"Compound score: {compound}")
            
            if compound >= 0.5:
                return "happy"
            elif compound <= -0.5:
                return "sad"
            elif -0.1 < compound < 0.1:
                return "neutral"
            else:
                return "angry"
        except Exception as e:
            self.logger.error(f"Sentiment analysis error: {e}")
            return "neutral"