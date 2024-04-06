import torch
from flask import Flask, jsonify
from flask import request
from urllib.request import urlopen
from config import *
from model import EffNetB0

from torchvision import transforms
from PIL import Image

app = Flask(__name__)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

def img_classification(img_path):
    try:
        if img_path.startswith("http"):
            # Open image from URL
            response = urlopen(img_path)
            img = Image.open(response)
        else:
            # Open image from local file path
            img =  Image.open(img_path)
    except (IOError, OSError):
        print(f"Error opening image: {img_path}")
        return None
    convert_tensor = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
    ])
    img = convert_tensor(img)
    img = img.unsqueeze(0)
    img.to(DEVICE)
    with torch.no_grad():
        pred = MODEL(img)    
    pred = torch.argmax(torch.softmax(pred, dim=1), dim=1)[0]
    return pred.item()



@app.route("/predict")
def predict():
    image_path = request.args.get("image_path")
    image_path = image_path
    prediction = img_classification(img_path=image_path)
    response = {}
    response["response"] = {
        "class": CLASS_NAME[prediction],
        "image_path":image_path
    }
    return jsonify(response)

if __name__ == "__main__":
    MODEL = EffNetB0(num_classes=NUM_CLASS)
    MODEL.load_state_dict(torch.load(PATH_TO_MODEL, map_location=torch.device(DEVICE))['model_state_dict'])
    MODEL.to(DEVICE)
    MODEL.eval()
    app.run(host='0.0.0.0', port=5000)