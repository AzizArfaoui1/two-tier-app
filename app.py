from flask import Flask, jsonify
import mysql.connector, os, time

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", "rootpass"),
        database=os.getenv("DB_NAME", "appdb")
    )

@app.route("/")
def index():
    return jsonify({
        "status": "ok",
        "message": "Hello from Flask + MySQL on VMware!"

    })

@app.route("/health")
def health():
    try:
        db = get_db()
        db.close()
        return jsonify({"db": "connected"}), 200
    except Exception as e:
        return jsonify({"db": "error", "detail": str(e)}), 500

@app.route("/data")
def data():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        db.close()
        return jsonify({"server_time": str(result[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
