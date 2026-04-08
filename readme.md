# 🛡️ Mini SOC Environment (OpenEnv Compatible)

## 📌 Overview

**Mini SOC Environment** is a real-world cybersecurity simulation designed for evaluating AI agents in Security Operations Center (SOC) workflows.

The environment simulates how analysts monitor system logs and decide whether to:

* Ignore benign activity
* Flag suspicious behavior
* Escalate critical threats

It follows the **OpenEnv standard interface** and supports agent interaction via:

* `step()`
* `reset()`
* `state()`

---

## 🎯 Motivation

Modern organizations rely on SOC analysts to detect and respond to cyber threats in real time. Automating this process requires structured environments where AI agents can:

* Interpret logs
* Make decisions under uncertainty
* Optimize actions based on feedback

This environment provides a **lightweight yet realistic benchmark** for evaluating such capabilities.

---

## 🧠 Real-World Task Simulation

This environment models a **log analysis workflow**, a core activity in cybersecurity operations.

Each step simulates:

* Incoming system logs
* Contextual metadata
* Decision-making under ambiguity

👉 This ensures the environment is **not a toy problem**, but a meaningful real-world task.

---

## ⚙️ OpenEnv Specification Compliance

The environment fully implements the OpenEnv interface:

### 🔹 Core API

* `reset()` → Initializes environment and returns first observation
* `step(action)` → Returns `(observation, reward, done, info)`
* `state()` → Returns current environment state

### 🔹 Typed Models (Pydantic)

* `Observation`
* `Action`
* `Reward`

---

## 📊 Observation Space

Each observation is a structured object:

```json
{
  "log": "string",
  "context": "string"
}
```

* **log** → system event message
* **context** → additional metadata

---

## 🎮 Action Space

The agent must return:

```json
{
  "decision": "ignore | flag | escalate",
  "confidence": 0.0 - 1.0
}
```

### 🔹 Actions

* `ignore` → benign
* `flag` → suspicious
* `escalate` → critical

### 🔹 Confidence (Advanced Feature ⭐)

* Represents certainty of the decision
* Enables **reward scaling and uncertainty modeling**

---

## 🧮 Reward Function (Advanced Design ⭐)

The reward function provides **continuous feedback across trajectory**:

| Scenario                           | Reward              |
| ---------------------------------- | ------------------- |
| Correct decision                   | `+1.0 × confidence` |
| Partial (flag instead of escalate) | `+0.5 × confidence` |
| Incorrect decision                 | `-0.2 × confidence` |

### ✅ Properties

* Dense reward (not sparse)
* Encourages calibrated confidence
* Penalizes incorrect high-confidence decisions
* Supports learning across steps

---

## 🧪 Tasks & Difficulty Levels

The environment includes **3 deterministic tasks**:

### 🟢 Easy

* Clear patterns
* Obvious classification

### 🟡 Medium

* Ambiguous logs
* Requires contextual reasoning

### 🔴 Hard

* Subtle attack indicators
* Requires deeper analysis

Each task:

* Has fixed ground truth
* Uses deterministic grading
* Produces score ∈ [0,1]

---

## 📈 Episode Design

* Multi-step environment
* Sequential log processing
* Ends when all tasks are completed

---

## 🤖 Baseline Inference Script

The project includes `inference.py` which:

* Uses **OpenAI client (required)**
* Connects via configurable environment variables
* Interacts with environment via API
* Outputs standardized logs:

```
[START]
[STEP]
[END]
```

### 🔹 Output Format Compliance

* Deterministic
* Reproducible
* Score normalized to [0,1]

---

## 🔐 Environment Variables

The inference script uses:

```env
HF_TOKEN=your_token
API_BASE_URL=https://router.huggingface.co/v1
MODEL_NAME=Qwen/Qwen2.5-72B-Instruct
```

* Uses OpenAI-compatible client
* Backend can be Hugging Face or OpenAI

---

## 🌐 API Endpoints

| Endpoint               | Description       |       |                   |
| ---------------------- | ----------------- | ----- | ----------------- |
| `GET /reset?level=easy | medium            | hard` | Start new episode |
| `POST /step`           | Take action       |       |                   |
| `GET /state`           | Get current state |       |                   |

---

## 🐳 Docker Support

The environment is fully containerized.

### Build:

```bash
docker build -t mini-soc-env .
```

### Run:

```bash
docker run -p 8000:8000 mini-soc-env
```

---

## 🤗 Hugging Face Deployment

The environment is deployed as a **Docker-based Hugging Face Space**:

👉 Live URL:
https://adityabiranje210-mini-soc-env.hf.space

* Fully functional API
* Accessible for evaluation
* Demonstrates real deployment

---

## 📦 Packaging & Multi-Mode Support

The project includes:

* `pyproject.toml`
* `uv.lock`
* `server/app.py`

This ensures:

* Multi-mode deployment compatibility
* Proper entrypoint definition
* Validator compliance

---

## ✅ OpenEnv Validator

The environment passes:

```bash
openenv validate
```

✔ Ready for multi-mode deployment
✔ Fully compliant with specification

---

## 📁 Project Structure

```
mini-soc-env/
│
├── models.py
├── env.py
├── tasks.py
├── main.py
├── inference.py
├── openenv.yaml
├── Dockerfile
├── requirements.txt
├── pyproject.toml
├── uv.lock
├── server/
│   └── app.py
└── README.md
```

---

## 🏆 Key Highlights

* Real-world cybersecurity simulation
* Advanced reward shaping with confidence
* Deterministic grading system
* OpenEnv full compliance
* Docker + HF deployment
* OpenAI client integration
* Multi-task difficulty design

---

## 📊 Evaluation Criteria Coverage

| Requirement           | Status |
| --------------------- | ------ |
| Real-world task       | ✅      |
| OpenEnv interface     | ✅      |
| 3+ tasks with graders | ✅      |
| Reward shaping        | ✅      |
| Baseline inference    | ✅      |
| Docker support        | ✅      |
| HF Space deployment   | ✅      |
| Documentation         | ✅      |

---

## 👨‍💻 Author

Aditya Biranje

---

## 🚀 Final Note

This environment is designed not just as a submission, but as a **scalable benchmark for evaluating AI agents in cybersecurity workflows**.

It demonstrates how structured environments can bridge the gap between **real-world tasks and agent learning systems**.
