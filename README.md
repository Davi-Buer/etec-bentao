# Docker Compose Exercise

A simple Node.js app + Redis running in Docker Compose.

## What you'll see

- Two containers running together (`app` and `redis`)
- The app stores messages and a visit counter in Redis
- Each student runs on their own port — no conflicts

## Setup

**1. Clone the repo**
```bash
git clone <repo-url>
cd etect-dockercompose-exercise
```

**2. Set your port** (use the number your instructor gave you)
```bash
cp .env.example .env
nano .env
```

Change `APP_PORT=8001` to your assigned port (e.g. `8002`, `8003`, ...).

**3. Start the containers**
```bash
docker compose up -d --build
```

**4. Open in the browser**
```
http://<VM-IP>:<your-port>
```

---

## Useful commands

```bash
# See running containers
docker ps

# See app logs
docker compose logs -f app

# Open a Redis CLI and inspect data
# (open the app in the browser and send some messages first!)
docker compose exec redis redis-cli

# Then type these commands at the 127.0.0.1:6379> prompt:
# KEYS *
# GET hits
# LRANGE messages 0 -1
# EXIT

# Stop everything
docker compose down
```

## Project structure

```
.
├── app.js            # Node.js HTTP server
├── Dockerfile        # How to build the app image
├── docker-compose.yml  # Two services: app + redis
└── .env              # Your port number (you create this from .env.example)
```
