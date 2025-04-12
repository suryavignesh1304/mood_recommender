import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyRecommender:
    def __init__(self, client_id, client_secret):
        # Initialize Spotify client
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=client_id, client_secret=client_secret
        ))

    def get_playlist(self, mood):
        """
        Recommend a playlist based on mood using specific playlist IDs.
        Returns playlist name and URL.
        """
        # Map moods to Spotify | https://open.spotify.com/playlist/<PLAYLIST_ID>
        mood_playlists = {
            "happy": {
                "id": "37i9dQZF1DX3rxVfibe1L0",  # Mood Booster
                "fallback_name": "Mood Booster",
                "fallback_url": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"
            },
            "sad": {
                "id": "54pvEYFocTlvIAQOfXSjqV",  # Alone Again
                "fallback_name": "Alone Again",
                "fallback_url": "https://open.spotify.com/track/54pvEYFocTlvIAQOfXSjqV"
            },
            "neutral": {
                "id": "5S2l0RAtGMMbgxbb1lS7IL",  # Chill Vibes
                "fallback_name": "Chill Vibes",
                "fallback_url": "https://open.spotify.com/playlist/5S2l0RAtGMMbgxbb1lS7IL"
            },
            "angry": {
                "id": "37i9dQZF1EIheh2DrZ2D3d",  # Rage
                "fallbacktrunc_name": "Rage",
                "fallback_url": "https://open.spotify.com/playlist/37i9dQZF1EIheh2DrZ2D3d"
            },
            "disgust": {
                "id": "37i9dQZF1EIcxMZBQ3y8Co",  # Dark Pop
                "fallback_name": "Dark Pop",
                "fallback_url": "https://open.spotify.com/playlist/37i9dQZF1EIcxMZBQ3y8Co"
            },
            "fear": {
                "id": "4aT2W9wchQKAimxVFSRIva",  # Spooky
                "fallback_name": "Spooky",
                "fallback_url": "https://open.spotify.com/track/4aT2W9wchQKAimxVFSRIva"
            },
            "surprise": {
                "id": "5UiT4e4DHwZrcVIXojU5um",  # Surprise Party
                "fallback_name": "Surprise Party",
                "fallback_url": "https://open.spotify.com/track/5UiT4e4DHwZrcVIXojU5um"
            }
        }

        # Get playlist info for the mood, default to neutral if mood not found
        playlist_info = mood_playlists.get(mood, mood_playlists["neutral"])

        try:
            # Fetch playlist by ID with market parameter
            playlist = self.sp.playlist(playlist_info["id"], market="US")
            return playlist["name"], playlist["external_urls"]["spotify"]
        except Exception as e:
            print(f"Spotify error for mood {mood}: {e}")
            return playlist_info["fallback_name"], playlist_info["fallback_url"]