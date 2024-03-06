import base64
from flask import Flask, request
from flask_cors import CORS
import cv2
import numpy as np

from Drowsiness_Detection import get_landmarks

app = Flask(__name__)
CORS(app)

def convert_base64_to_image(base64_image):
    image_bytes = base64.b64decode(base64_image)
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return image

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello from Walker."

@app.route('/get_landmarks', methods=['GET', 'POST'])
def landmarks():
    data = request.get_json()
    base64_image = data.get("image")
    image = convert_base64_to_image(base64_image)
    landmarks = get_landmarks(image)
    if landmarks:
        return {"landmarks":landmarks,"status":"Detected"}
    else:
        return {"status":"Not detected"}


if __name__ == '__main__':
    app.run(debug=True)