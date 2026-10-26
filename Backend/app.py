from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/submit", methods=["POST"])
def handle_form():
  data = request.get_json(silent=True) or {}
  username = data.get("username", "anonymous")
  email = data.get("email", "no email provided")

  print(f"Received data -> User: {username}, Email: {email}", flush=True)

  return jsonify({
      "status": "success",
      "message": f"Hello {username}! Data received successfully.",
  })


@app.route("/health", methods=["GET"])
def health():
  return jsonify({"status": "running"}), 200


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=False)
