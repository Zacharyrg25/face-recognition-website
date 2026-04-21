from flask import Flask, jsonify, render_template, request
import cv2
import numpy as np
from mtcnn.mtcnn import MTCNN

app = Flask(__name__)

# Load Haar.
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load MTCNN.
face_mtcnn = MTCNN()


@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html")


@app.route("/detect", methods=["POST"])
def detect():
    """Detect faces in an uploaded image using the selected method."""
    # Read the uploaded image.
    file = request.files["image"]
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    mode = request.form["mode"]
    boxes = []

    # Haar requires a grayscale image.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if mode == "Haar":
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(30, 30),
        )
        for (x, y, w, h) in faces:
            boxes.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h)})

    elif mode == "MTCNN":
        faces = face_mtcnn.detect_faces(img)
        for face in faces:
            x, y, w, h = face["box"]
            boxes.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h)})

    return jsonify({"faces": boxes})


if __name__ == "__main__":
    app.run(debug=True)