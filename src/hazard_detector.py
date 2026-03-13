import cv2
import numpy as np

def detect_hazard(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)

    hazard_score = np.sum(edges)

    if hazard_score > 50000:
        return "Potential Hazard Detected"
    else:
        return "Low Hazard Visibility"
