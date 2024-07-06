from machine_learning.image_predictor import ImagePredictor

# Initialize the predictor
predictor = ImagePredictor()

image_path = '2017-05-15T19-48-56.jpg'

# Get the prediction results
result_1, result_2, result_3 = predictor.predict(image_path)

# Display the results
print(f'result_1: {result_1}')
print(f'result_2: {result_2}')
print(f'result_3: {result_3}')
