# Rate Limiter using Redis

This is a simple Flask-based rate limiter that uses Redis to track and control the number of API requests a user can make within a specific time window.

## 🚀 Features
- IP-based request limiting
- Redis-backed in-memory store
- Lightweight and fast
- Easy to extend with sliding windows or token buckets

## 🛠 Tech Stack
- Python
- Flask
- Redis
- Docker (for Redis container)

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/rate-limiter-redis.git
cd rate-limiter-redis
```

---

### 2. Create and Activate Virtual Environment
```bash

python -m venv venv
.\venv\Scripts\activate
```

---

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4. Run Redis via Docker
```bash

docker run --name redis-rate-limiter -p 6379:6379 -d redis
```

---

### 5. Run Flask App
```bash

python app.py
```
> Access the rate-limited API at:
👉 http://127.0.0.1:5000/api

---

📦 Example Rate Limit
Max: 5 requests per 60 seconds per IP

On exceeding, returns 429 Too Many Requests with try_after_seconds

---

📄 License
[MIT]