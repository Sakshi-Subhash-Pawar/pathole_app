pothole-detection-app/
│
├── app.py # Flask app entry point
├── static/ # Static files (CSS, JS)
├── templates/ # HTML templates (Jinja2)
├── utils/
│ ├── detection.py # Pothole detection logic using OpenCV
│ └── estimation.py # Cement estimation based on size
└── uploads/ # Uploaded videos (if any)

# 🛣️ Pothole Detection and Cement Estimation Web App (Flask + OpenCV)

This project is a Flask-based web application that detects potholes in road surfaces from video files or live camera feeds. It utilizes computer vision techniques to identify potholes, calculate their count and approximate size, and estimate the amount of cement required for repair.

---

## 🚀 Features

- 📹 Accepts input via:
  - Uploaded video files
  - Live camera feed (webcam)
- 🔍 Detects potholes using OpenCV
- 📏 Calculates:
  - Number of potholes
  - Size of each pothole (approximate area)
- 🧱 Estimates cement required for repairs based on total pothole volume
- 🖥️ Web interface built with Flask for easy interaction

---

## 🧰 Tech Stack

- **Python**
- **Flask** (Web Framework)
- **OpenCV** (Computer Vision)
- **NumPy** (Numerical Operations)
- **HTML/CSS** (Front-end UI)

---

## 📦 Cement Estimation Logic

The application assumes:
- Average pothole depth = *X* cm (can be configured)
- Volume of each pothole = Area × Depth
- Cement required is calculated using standard construction formulas.

You can modify this logic in `utils/estimation.py`.

---

## 🖼️ Sample Workflow

1. Upload or stream video
2. Potholes are detected frame-by-frame
3. Area of each pothole is computed
4. Cement estimation is calculated
5. Final report with total potholes, sizes, and cement quantity is displayed

---

## 📂 Project Structure


