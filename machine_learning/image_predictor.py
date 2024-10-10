import json
import tensorflow as tf
from PIL import Image
import numpy as np
from efficientnet.tfkeras import EfficientNetB0

from database.models import Disease

class ImagePredictor:
    def __init__(self, diagnosis_type):
        with open('machine_learning/config.json', 'r') as config_file:
            config = json.load(config_file)
        self.config = config[diagnosis_type]
        all_diseases = Disease.DiseaseModel().get_all_diseases_by_diagnosis_type(diagnosis_type=diagnosis_type)
        self.labels = [disease['nama_penyakit'] for disease in all_diseases]
        self.model = tf.keras.models.load_model(self.config['model'])
        self.preprocessing_function = eval(self.config['preprocessing_function'])

    def preprocess_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize(eval(self.config['image_size']))
        img = np.array(img)
        img = self.preprocessing_function(img) 
        img = np.expand_dims(img, axis=0)
        return img

    def predict(self, image_path):
        processed_image = self.preprocess_image(image_path)
        predictions = self.model.predict(processed_image)
        top_3_indices = np.argsort(predictions[0])[-3:][::-1]
        top_3_probabilities = predictions[0][top_3_indices]
        top_3_labels = [self.labels[i] for i in top_3_indices]
        result = [(top_3_labels[i], top_3_probabilities[i]) for i in range(3)]
        result_1, result_2, result_3 = result
        return result_1, result_2, result_3