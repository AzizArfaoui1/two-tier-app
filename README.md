# Two-Tier CI/CD Pipeline — Flask + MySQL + Docker + Jenkins

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-red)
![Flask](https://img.shields.io/badge/Backend-Flask-lightgrey)
![MySQL](https://img.shields.io/badge/Database-MySQL%208-orange)
![Free](https://img.shields.io/badge/Cost-%240%2Fmo-brightgreen)

A fully automated CI/CD pipeline deploying a two-tier web application (Flask + MySQL) using Docker Compose, Jenkins, and GitHub Webhooks — running entirely on a local VMware VM with zero cloud cost.

---

## Architecture

```
Developer (git push)
       │
       ▼
   GitHub Repo
       │  webhook
       ▼
     ngrok
  (public tunnel)
       │
       ▼
  Jenkins :8080
  (VMware VM)
       │
   Pipeline:
   ┌────────────┐
   │ 1. Clone   │
   │ 2. Build   │
   │ 3. Deploy  │
   │ 4. Test    │
   └────────────┘
       │
       ▼
Docker Compose
  ┌──────────┐    ┌──────────┐
  │  Flask   │───▶│  MySQL   │
  │ :5000    │    │ :3306    │
  └──────────┘    └──────────┘
       │
       ▼
  App live at
http://192.168.x.x:5000
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11 + Flask 3.0 |
| Database | MySQL 8.0 |
| Containerization | Docker + Docker Compose |
| CI/CD | Jenkins 2.555 |
| Source Control | GitHub |
| Tunnel | ngrok (free tier) |
| Virtualization | VMware Workstation Player |
| OS | Ubuntu 22.04 LTS |

---

## Project Structure

```
two-tier-app/
├── app.py                  # Flask application (3 endpoints)
├── requirements.txt        # Python dependencies
├── Dockerfile              # Flask container image
├── docker-compose.yml      # Orchestrates Flask + MySQL
├── Jenkinsfile             # CI/CD pipeline definition
└── tests/
    └── test_app.py         # Integration tests (pytest)
```

---

## Pipeline Stages

```
Checkout SCM → Clone → Build → Deploy → Test → Post Actions
     ✅           ✅      ✅       ✅      ✅         ✅
```

| Stage | What it does |
|---|---|
| **Checkout SCM** | Jenkins fetches Jenkinsfile from GitHub |
| **Clone** | Pulls latest code from main branch |
| **Build** | Builds Flask Docker image with `docker compose build` |
| **Deploy** | Starts Flask + MySQL containers with `docker compose up -d` |
| **Test** | Runs 4 integration tests with pytest against live app |
| **Post Actions** | Reports success or tears down containers on failure |

---

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Returns app status and welcome message |
| `/health` | GET | Checks MySQL database connectivity |
| `/data` | GET | Returns current MySQL server timestamp |

---

## How to Run Locally

### Prerequisites
- VMware Workstation Player (or VirtualBox)
- Ubuntu 22.04 VM with 4GB+ RAM
- Docker + Docker Compose v2
- Jenkins (Java 21)
- ngrok account (free)

### 1. Clone the repo
```bash
git clone https://github.com/AzizArfaoui1/two-tier-app.git
cd two-tier-app
```

### 2. Start the app manually
```bash
docker compose up -d --build
```

### 3. Test the app
```bash
curl http://localhost:5000/
curl http://localhost:5000/health
curl http://localhost:5000/data
```

### 4. Run tests
```bash
python3 -m pytest tests/ -v
```

---

## CI/CD Flow

Every `git push` to `main` automatically:

1. GitHub sends a webhook to Jenkins via ngrok tunnel
2. Jenkins pulls the latest code
3. Docker builds a fresh Flask image
4. Docker Compose starts Flask + MySQL containers
5. pytest runs 4 integration tests against the live app
6. On success: app stays running on port 5000
7. On failure: containers are stopped automatically

---

## Key Technical Decisions

**Why Docker Compose healthcheck?**
MySQL takes ~30s to initialize. The `healthcheck` + `depends_on: condition: service_healthy` ensures Flask only starts after MySQL is fully ready — preventing connection errors.

**Why ngrok?**
The VM has no public IP. ngrok creates a public HTTPS tunnel so GitHub webhooks can reach Jenkins running inside the local VM.

**Why VMware instead of AWS?**
Full control, zero cost, no card required, and 8x more RAM than AWS free tier (t2.micro = 1GB). Every concept learned is 100% transferable to any cloud provider.

---

## Cost

| Component | Cost |
|---|---|
| VMware Workstation Player | $0 (free for personal use) |
| Ubuntu 22.04 | $0 (open source) |
| Docker + Docker Compose | $0 (open source) |
| Jenkins | $0 (open source) |
| ngrok (free tier) | $0 |
| GitHub | $0 |
| **Total** | **$0/month** |

---

## Author

**Aziz Arfaoui**
- GitHub: [@AzizArfaoui1](https://github.com/AzizArfaoui1)
- Email: arfandarf2222@gmail.com
