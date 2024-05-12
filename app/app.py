from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import os
import tensorflow as tf

app = Flask(__name__)

# Function to preprocess the image
def preprocess_image(img):
    img = cv2.resize(img, (200, 50))
    img = img.astype(np.float32) # Convert to float32
    img = img[..., np.newaxis] # Add channel dimension
    img = img / 255.0 # Normalize
    return img

# Load the saved model
MODEL_PATH = "./models/captcha-ocr-model/1"
model = tf.saved_model.load(MODEL_PATH)

# Load the characters_keys list from the text file
CHARACTERS_KEYS_PATH = os.path.join(MODEL_PATH, "assets", "characters_keys.txt")
with open(CHARACTERS_KEYS_PATH, 'r') as f:
    characters_keys = [line.strip() for line in f]

# Set the upload folder
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded"
    file = request.files['file']
    if file.filename == '':
        return "No file selected"
    if file:
        # Save uploaded image to a temporary location
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Read and preprocess the uploaded image
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        preprocessed_img = preprocess_image(image)

        # Add a new axis to the input image array
        expanded_img = np.expand_dims(preprocessed_img, axis=0)
        predictions = model(expanded_img)
        predicted_chars = ''.join(characters_keys[np.argmax(pred)] for pred in predictions)

        return render_template('prediction.html', filename=filename, predicted_chars=predicted_chars)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')