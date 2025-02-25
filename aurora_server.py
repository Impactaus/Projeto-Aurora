from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Aurora está online e funcionando!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)