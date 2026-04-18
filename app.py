from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np

from mtcnn.mtcnn import MTCNN # NEW NEW NEW

app = Flask(__name__)

# Load the Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load MTCNN # NEW NEW NEW
face_mtcnn = MTCNN() # NEW NEW NEW

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/detect', methods=['POST'])
def detect():
    # Read the uploaded image
    file = request.files['image']
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # Read the mode # NEW NEW NEW
    mode = request.form['mode'] # NEW NEW NEW

    # Convert to grayscale and detect faces
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    boxes = []

    # NEW NEW NEW SECTION
    if mode == "haar":
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30)) # OLD
        for (x, y, w, h) in faces:
            boxes.append({'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)})
    elif mode == "mtcnn":
        faces = face_mtcnn.detect_faces(img)
        for face in faces:
            x, y, w, h = face['box']
            boxes.append({'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)})
    # NEW NEW NEW SECTION

    # OLD
    # # Build the list of face boxes to send back
    # boxes = []
    # for (x, y, w, h) in faces:
    #     boxes.append({'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)})
    # OLD

    return jsonify({'faces': boxes})

if __name__ == '__main__':
    app.run(debug=True)