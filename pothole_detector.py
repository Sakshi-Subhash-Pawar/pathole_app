
import cv2
import numpy as np

def detect_potholes(video_path, debug=False):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    pothole_count = 0
    pothole_data = []

    # Constants for conversion (dummy values - replace after calibration)
    PIXELS_PER_METER = 100  # Adjust based on camera and road calibration
    FRAME_INTERVAL = 10     # Process every 10th frame

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1

        if frame_count % FRAME_INTERVAL != 0:
            continue

        # Preprocessing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area_px = cv2.contourArea(cnt)
            if 500 < area_px < 5000:
              
                area_m2 = (area_px / (PIXELS_PER_METER ** 2))
                depth_m = 0.08 

                pothole_data.append({
                    'frame': frame_count,
                    'area_px': area_px,
                    'area_m2': round(area_m2, 4),
                    'depth_m': round(depth_m, 3),
                })

                pothole_count += 1

                if debug:
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if debug:
            debug_frame_path = f'static/debug/frame_{frame_count}.jpg'
            cv2.imwrite(debug_frame_path, frame)

    cap.release()

    return {
        "count": pothole_count,
        "sizes": [round(p['area_m2'], 3) for p in pothole_data],
        "potholes": pothole_data
    }
