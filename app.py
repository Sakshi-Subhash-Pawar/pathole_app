

from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import logging
from model.pothole_detector import detect_potholes
from utils.cement_estimator import estimate_cement

# Configuration
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'secret_key_for_session'

# Logging setup
logging.basicConfig(level=logging.INFO)

# Helper to check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'video' not in request.files:
            flash('No video part in request')
            return redirect(request.url)

        file = request.files['video']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            logging.info(f"Processing file: {filename}")
            pothole_data = detect_potholes(filepath)
            cement_required = estimate_cement(pothole_data)

            return render_template(
                'index.html',
                pothole_data=pothole_data,
                cement=round(cement_required, 2),
                video_path=filepath
            )
        else:
            flash('Unsupported file format.')
            return redirect(request.url)

    return render_template('index.html')
    
if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
