# Mini SOC Environment (OpenEnv)

## Overview
Mini SOC Environment is a cybersecurity simulation where an AI agent acts as a Security Operations Center (SOC) analyst. The agent analyzes system logs and decides whether to ignore, flag, or escalate potential threats.

This environment is designed to evaluate decision-making abilities of AI agents in real-world cybersecurity workflows.

---

## Motivation
Security analysts constantly monitor logs to detect anomalies and prevent attacks. Automating this process using AI agents requires structured environments for evaluation. This project provides a lightweight but realistic simulation for such tasks.

---

## Environment Design

### Observation Space
Each observation consists of:
- `log`: A system log message
- `context`: Additional contextual information

### Action Space
Discrete actions:
- `ignore`
- `flag`
- `escalate`

### Reward Function
- `1.0` → Correct decision  
- `0.5` → Partially correct (flag instead of escalate)  
- `0.0` → Incorrect decision  

Rewards provide meaningful feedback across steps.

---

## Tasks

### Easy
- Clear and obvious patterns
- Minimal reasoning required

### Medium
- Ambiguous logs
- Requires contextual understanding

### Hard
- Subtle attack indicators
- Requires deeper reasoning

---

## API Endpoints

- `GET /reset?level=easy|medium|hard`
- `POST /step`
- `GET /state`

---

## Running Locally

```bash
uvicorn main:app --reload