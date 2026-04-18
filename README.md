# 🎯 Face Detection Web App

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black)
![OpenCV](https://img.shields.io/badge/OpenCV-Face%20Detection-green)

A Flask-based web application that detects faces in images using two different methods:

- Haar Cascades (OpenCV)
- MTCNN (Deep Learning)

Users can upload images, choose a detection method, and visualize results directly in the browser.

---

## 📸 Demo

<!-- Add your screenshots here later -->
![Homepage](assets/home.png)
![Haar Detection](assets/haar.png)
![MTCNN Detection](assets/mtcnn.png)

---

## 🎥 Demo GIF

<!-- Add a GIF here later -->
![Demo](assets/demo.gif)

---

## ✨ Features

- Upload and preview images
- Choose between Haar and MTCNN detection
- Real-time face bounding boxes
- Canvas-based visualization in the browser

---

## 🧪 Usage

1. Upload an image
2. Select a detection method (Haar or MTCNN)
3. Click "Detect Faces"
4. View results drawn directly on the image

---

## 🧠 Detection Methods

**Haar Cascades**
- Fast and lightweight
- Traditional computer vision method
- Less accurate on complex images

**MTCNN**
- Deep learning-based
- More accurate detection
- Slightly slower but more robust

---

## 🚀 Setup Instructions

### 1. Clone the repository

git clone <your-repo-url>  
cd <your-project-folder>

---

### 2. Create a virtual environment

python3.12 -m venv .venv

---

### 3. Activate the virtual environment

Mac/Linux:  
source .venv/bin/activate  

Windows:  
.venv\Scripts\activate  

---

### 4. Install dependencies

pip install -r requirements.txt

---

### 5. Run the app

python app.py

---

### 6. Open in browser

http://127.0.0.1:5000/

---

## 📁 Project Structure

Face Detection Website/  
├── app.py  
├── requirements.txt  
├── .gitignore  
├── README.md  
├── templates/  
│   ├── index.html  
│   └── about.html  
├── static/  
│   ├── style.css  
│   └── script.js  
└── assets/  

---

## ⚠️ Notes

- The `.venv/` folder is not included in the repository
- Make sure to activate the virtual environment before running the app
- This project uses Python 3.12

---

## 🛠️ Tech Stack

- Python
- Flask
- OpenCV
- MTCNN
- TensorFlow
- JavaScript (Canvas API)

---

## 💡 Motivation

Built to explore computer vision techniques and full-stack integration using Flask and JavaScript.

---

## 🚀 Future Improvements

- Improved UI/UX design
- Face confidence scores
- Image upload history
- Cloud deployment