import cv2
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow.keras.backend as K
import logging
import h5py
import os
import threading

class EmotionDetector:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, model_path=r"models\FER2013.h5"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(EmotionDetector, cls).__new__(cls)
                cls._instance._initialize(model_path)
        return cls._instance

    def _initialize(self, model_path):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        try:
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found at: {model_path}")
                
            self.logger.info("Clearing TensorFlow session...")
            K.clear_session()
            
            self.logger.info(f"Checking model file: {model_path}")
            with h5py.File(model_path, 'r') as f:
                if 'model_config' not in f.attrs:
                    raise ValueError("Invalid .h5 file: missing model_config")
            
            self.logger.info("Loading model...")
            self.model = load_model(model_path, compile=False)
            self.logger.info("Model loaded successfully.")
            
            self.emotion_labels = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]
            self.logger.info(f"Model input shape: {self.model.input_shape}")
            self.logger.info(f"Model output shape: {self.model.output_shape}")
            
            self.logger.info("Loading Haar Cascade classifier...")
            cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            self.face_cascade = cv2.CascadeClassifier(cascade_path)
            if self.face_cascade.empty():
                raise RuntimeError(f"Failed to load Haar Cascade from: {cascade_path}")
            self.logger.info("Haar Cascade loaded successfully.")
                
        except Exception as e:
            self.logger.error(f"Failed to initialize EmotionDetector: {e}")
            raise

    def detect_emotion(self, image_path):
        try:
            self.logger.info(f"Processing image: {image_path}")
            if not os.path.exists(image_path):
                self.logger.warning(f"Image file not found: {image_path}")
                return "neutral"
                
            image = cv2.imread(image_path)
            if image is None:
                self.logger.warning("Failed to read image.")
                return "neutral"

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            if len(faces) == 0:
                self.logger.warning("No faces detected.")
                return "neutral"

            (x, y, w, h) = faces[0]
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (48, 48))
            face = face.astype("float32") / 255.0
            face = np.expand_dims(face, axis=0)
            face = np.expand_dims(face, axis=-1)

            self.logger.info("Predicting emotion...")
            predictions = self.model.predict(face, verbose=0)[0]
            dominant_emotion = self.emotion_labels[np.argmax(predictions)]
            self.logger.info(f"Detected emotion: {dominant_emotion}")
            return dominant_emotion
        except Exception as e:
            self.logger.error(f"Emotion detection error: {e}")
            return "neutral"