# import model package
import logging
import torch
from simpletransformers.t5 import T5Model, T5Args
import os

# load flaskapi
from flask import Flask, request, jsonify
import json

# load model
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)
model_args = T5Args()
model_args.max_length = 100
model_args.length_penalty = 1
model_args.num_beams = 10
device = torch.cuda.is_available()
model = T5Model("mt5", 'SigmarAI/MT5', args=model_args, use_cuda=device)

def predict(text):
    to_predict = [text]
    predictions = model.predict(to_predict)
    return predictions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        json_data = request.get_json()
        if not json_data:
            return jsonify({"error": "no data"})
        try:
            prediction = predict(json_data["text"])
            data_predicted = {"prediction": prediction}
            print(data_predicted)
            return jsonify(data_predicted)
        except Exception as e:
            return jsonify({"error": str(e)})
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)