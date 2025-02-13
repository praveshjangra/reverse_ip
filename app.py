from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# MySQL Connection
DB_HOST = os.getenv("DB_HOST", "mysql.default.svc.cluster.local")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "ipdb")

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# Route to get & store reversed IP
@app.route("/", methods=["GET"])
def get_reversed_ip():
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    reversed_ip = ".".join(client_ip.split(".")[::-1])

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ip_records (original_ip, reversed_ip) VALUES (%s, %s)", (client_ip, reversed_ip))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"original_ip": client_ip, "reversed_ip": reversed_ip})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
