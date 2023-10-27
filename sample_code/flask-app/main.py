import os
import requests
import flask
from flask import Flask, jsonify, Response

from dotenv import load_dotenv
load_dotenv()

PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/get_image/<image>", methods=["GET", "POST"])
def get_image(image):
    if flask.request.method == "POST":
        return Response(status=501, response="Method not implemented")
    
    url = f"https://api.pexels.com/v1/search?query={image}"
    if image == "cat":
        return Response(status=404, response="No cats allowed!")
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    response = requests.get(url=url, headers=headers)
    return jsonify(response.json())
        
if __name__ == "__main__":
    app.run(port=8080, debug=True)
