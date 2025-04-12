class MoodRecommender:
    def generate_recommendations(self, mood):
        """
        Generate recommendations based on mood.
        Returns dict with playlist, lighting, activity, and quote.
        """
        lighting_suggestions = {
            "happy": "Bright yellow",
            "sad": "Soft blue",
            "neutral": "Warm white",
            "angry": "Cool green"
        }
        activity_suggestions = {
            "happy": "Dance or go for a run",
            "sad": "Meditate or journal",
            "neutral": "Read a book",
            "angry": "Try deep breathing"
        }
        return {
            "lighting": lighting_suggestions.get(mood, "Warm white"),
            "activity": activity_suggestions.get(mood, "Relax"),
        }