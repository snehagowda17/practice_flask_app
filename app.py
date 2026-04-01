from flask import Flask, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"


@app.route("/")
def home():
    return jsonify({
        "message": "Flask JSONPlaceholder API is running",
        "routes": ["/posts", "/comment", "/albums"]
        "data":["successfully committed"]
    })


@app.route("/posts")
def get_posts():
    try:
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route("/comment")
def get_comments():
    try:
        response = requests.get(f"{BASE_URL}/comments")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


@app.route("/albums")
def get_albums():
    try:
        response = requests.get(f"{BASE_URL}/albums")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
