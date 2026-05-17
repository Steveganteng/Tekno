from flask import Flask, jsonify
import json
import io

app = Flask(__name__)

def load_all_medicines():
    try:
        with io.open("all_medicines_recommendations.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

@app.route("/")
def dashboard():
    with io.open("dashboard_all_medicines.html", "r", encoding="utf-8-sig") as f:
        html = f.read()
    return html

@app.route("/all_medicines_recommendations.json")
def get_all_medicines_json():
    data = load_all_medicines()
    return jsonify(data)

if __name__ == "__main__":
    print("Starting Flask app...")
    print("Open browser: http://localhost:5000")
    app.run(debug=False, port=5000, host="127.0.0.1")