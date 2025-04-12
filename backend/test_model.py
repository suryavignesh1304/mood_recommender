# Save as test_model.py
from tensorflow.keras.models import load_model
import tensorflow.keras.backend as K

K.clear_session()
try:
    model = load_model("E:\mood_recommender\models\FER2013.h5", compile=False)
    print("Model loaded successfully")
    print("Input shape:", model.input_shape)
    print("Output shape:", model.output_shape)
except Exception as e:
    print(f"Error loading model: {e}")