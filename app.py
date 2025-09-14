from flask import Flask, request, jsonify, render_template , redirect, url_for
from dotenv import load_dotenv
import pymongo
import os
load_dotenv()
from pymongo import MongoClient
MONGO_URI= os.getenv('MONGO_URI')
client =pymongo.MongoClient(MONGO_URI)
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"Connection failed: {e}")
db = client["TuteDude"]

app = Flask(__name__)

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    data = request.json
    item_name = data.get("itemName")
    item_desc = data.get("itemDescription")

    if not item_name or not item_desc:
        return jsonify({"error": "Missing fields"}), 400

    db["To_do"].insert_one({"name": item_name, "description": item_desc})
    return jsonify({"message": "To-Do item saved successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")