from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

# Connect to Redis
r = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

# Rate Limit Config
RATE_LIMIT = 5  # max requests
TIME_WINDOW = 60  # time window in seconds


@app.route("/api", methods=["GET"])
def api():
    client_ip = request.remote_addr
    key = f"rate_limit:{client_ip}"

    current = r.get(key)

    if current is None:
        r.set(key, 1, ex=TIME_WINDOW)
    elif int(current) < RATE_LIMIT:
        r.incr(key)
    else:
        ttl = r.ttl(key)
        return jsonify({"error": "Rate limit exceeded", "try_after_seconds": ttl}), 429

    return jsonify({"message": "Request successful!"})


if __name__ == "__main__":
    app.run(debug=True)
