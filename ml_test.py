from machine_learning.image_predictor import ImagePredictor

# Initialize the predictor with the model path
model_path = './machine_learning/models/1-model_tuning224_128_adam.h5'
predictor = ImagePredictor(model_path)

# Path to your image
image_path = '2017-05-15T19-48-56.jpg'
# image_path = './N1.jpg'  # Uncomment this line to use the second image

# Get the prediction results
result_1, result_2, result_3 = predictor.predict(image_path)

# Display the results
print(f'result_1: {result_1}')
print(f'result_2: {result_2}')
print(f'result_3: {result_3}')
