import tensorflow as tf
from PIL import Image
import numpy as np
from efficientnet.tfkeras import EfficientNetB0

class ImagePredictor:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.labels = [
            'Aerotitis Barotrauma', 'Cerumen', 'Corpus Alienum', 'M Timpani normal', 
            'Myringitis Bulosa', 'Normal', 'OE Difusa', 'OE Furunkulosa', 'OMA Hiperemis', 
            'OMA Oklusi Tuba', 'OMA Perforasi', 'OMA Resolusi', 'OMA Supurasi', 'OMed Efusi', 
            'OMedK Resolusi', 'OMedK Tipe Aman', 'OMedK Tipe Bahaya', 'Otomikosis', 
            'Perforasi Membran Tympani', 'Tympanosklerotik'
        ]

    def preprocess_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((224, 224))
        img = np.array(img) / 255.0  # Normalize pixel values to [0, 1]
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        return img

    def predict(self, image_path):
        # Preprocess the image
        processed_image = self.preprocess_image(image_path)
        
        # Make predictions
        predictions = self.model.predict(processed_image)
        
        # Get the top 3 predicted class indices
        top_3_indices = np.argsort(predictions[0])[-3:][::-1]
        top_3_probabilities = predictions[0][top_3_indices]
        top_3_labels = [self.labels[i] for i in top_3_indices]
        
        # Save the results as a list of tuples
        result = [(top_3_labels[i], top_3_probabilities[i]) for i in range(3)]
        
        # Unpack the results into separate variables
        top_1, top_2, top_3 = result
        
        return top_1, top_2, top_3

# Save the above class in a file named image_predictor.py
