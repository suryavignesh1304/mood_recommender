import requests

class QuoteGenerator:
    def get_quote(self, mood):
        """
        Fetch a motivational quote based on mood.
        Returns quote and author.
        """
        mood_keywords = {
            "happy": "happiness",
            "sad": "inspirational",
            "neutral": "motivational",
            "angry": "calm"
        }
        try:
            response = requests.get("https://api.quotable.io/random?tags=" + mood_keywords.get(mood, "motivational"))
            data = response.json()
            return data["content"], data["author"]
        except Exception as e:
            print(f"Quote API error: {e}")
            return "Stay positive!", "Unknown"