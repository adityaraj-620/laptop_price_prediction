from flask import Flask, request, jsonify, send_from_directory
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__, static_folder=".")
CORS(app)

# Load the trained model
with open("laptop_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({"predicted_price": round(prediction)})

# Serve index.html on root
@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

# Serve static files like CSS, JS
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
