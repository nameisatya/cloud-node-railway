from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "✅ Cloud Node is running!"

@app.route("/receive_from_fog", methods=["POST"])
def receive_from_fog():
    data = request.json
    print(f"📥 Received model from Fog Node: {data}")
    return jsonify({"message": "Model received at Cloud Node"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
