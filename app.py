from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["simple_app"]
collection = db["texts"]

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            collection.insert_one({"text": text})
        return redirect('/')
    
    texts = list(collection.find().sort("_id", -1))
    return render_template("index.html", texts=texts)

if __name__ == '__main__':
    app.run(debug=True)
