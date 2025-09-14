from flask import Flask, jsonify
import json
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello from Flask! Go to /api to see the data."

# API route
@app.route("/api")
def get_data():
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'data.json')
    with open(data_file_path) as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)