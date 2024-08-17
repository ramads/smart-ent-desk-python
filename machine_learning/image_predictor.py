import tensorflow as tf
from PIL import Image
import numpy as np
from efficientnet.tfkeras import EfficientNetB0

from database.models import Disease

class ImagePredictor:
    def __init__(self, diagnosis_type):
        model_path = f'./machine_learning/models/{diagnosis_type}.h5'
        all_diseases = Disease.DiseaseModel().get_all_diseases_by_diagnosis_type(diagnosis_type=diagnosis_type)
        self.labels = [disease['nama_penyakit'] for disease in all_diseases]
        print(self.labels)
        self.model = tf.keras.models.load_model(model_path)

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
        print("test", predictions)
        top_3_indices = np.argsort(predictions[0])[-3:][::-1]
        top_3_probabilities = predictions[0][top_3_indices]
        top_3_labels = [self.labels[i] for i in top_3_indices]
        
        # Save the results as a list of tuples
        result = [(top_3_labels[i], top_3_probabilities[i]) for i in range(3)]
        
        # Unpack the results into separate variables
        result_1, result_2, result_3 = result
        
        return result_1, result_2, result_3
