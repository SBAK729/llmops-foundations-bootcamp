# LLMOps Foundations Bootcamp 🚀

This repo contains a practical LLMOps framework demo for a customer-facing chatbot.

---

## 📂 Repo Structure
- `/src/monitoring.py` → Logs chatbot responses, detects PII, tracks latency/errors  
- `/src/feedback_collector.py` → Collects feedback from users/PMs  
- `/docs/lifecycle_map.md` → LLMOps lifecycle diagram & explanations  
- `/docs/monitoring_flow.md` → How monitoring works step by step  
- `requirements.txt` → Dependencies  
- `README.md` → Docs, onboarding, rollback, design decisions  

---

## 🔄 LLMOps Lifecycle
See [`docs/lifecycle_map.md`](docs/lifecycle_map.md) for the full Mermaid diagram.

---

## ⚙️ Usage

### Run Monitoring
```bash
python src/monitoring.py


### Feedback Collector
```bash
python src/feedback_collector.py


### 🌐 Versioning & Rollback

Branches: main (dev), stable (production-ready)

To rollback:
```bash
git checkout stable
git reset --hard stable
git push origin main --force

### 🔐 Privacy & Compliance

Regex scanning for emails & phone numbers in chatbot outputs

Logs stored locally; in production, would route to secure logging service

Feedback anonymized with uuid feedback IDs


### 🧩 Design Decisions

Simple regex-based PII detection (extendable later with NLP libraries)

JSONL for feedback storage (lightweight, easy to parse)

Minimal dependencies for fast onboarding


### 👩‍💻 Onboarding

Clone repo

Create virtualenv

Run monitoring & feedback demos

Explore logs in chatbot_logs.txt and feedback_records.jsonl


###  📚 References

[LLMOps Masterclass Video, Part 1, 00:42:30 – Monitoring Basics]

[LLMOps Masterclass Video, Part 2, 01:05:10 – Feedback Loops]
