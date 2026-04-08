# final submission fix
from dotenv import load_dotenv
load_dotenv()

import requests
import os
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
API_KEY = os.getenv("HF_TOKEN")

client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

BASE_URL = "http://127.0.0.1:8000"

TASK_NAME = "mini-soc"
ENV_NAME = "mini-soc-env"

def log_start():
    print(f"[START] task={TASK_NAME} env={ENV_NAME} model={MODEL_NAME}", flush=True)

def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)

def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={rewards_str}", flush=True)

def get_action(log, context):
    prompt = f"""
You are a cybersecurity analyst.

Log: {log}
Context: {context}

Choose ONE action:
ignore, flag, escalate

Return format:
action,confidence (e.g., flag,0.8)
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10,
            temperature=0
        )

        output = response.choices[0].message.content.strip().lower()

        action, confidence = output.split(",")

        if action not in ["ignore", "flag", "escalate"]:
            action = "ignore"

        confidence = float(confidence)
        confidence = max(0.0, min(1.0, confidence))

        return action, confidence

    except:
        return "ignore", 0.5


def run_episode(level="easy"):
    rewards = []
    step_count = 0

    log_start()

    obs = requests.get(f"{BASE_URL}/reset?level={level}").json()
    done = False

    while not done:
        step_count += 1

        action, confidence = get_action(obs["log"], obs["context"])

        response = requests.post(
            f"{BASE_URL}/step",
            json={
                "decision": action,
                "confidence": confidence
            }
        ).json()

        reward = response["reward"]
        done = response["done"]

        rewards.append(reward)

        log_step(step_count, f"{action}({confidence})", reward, done)

        obs = response["observation"] if not done else None

    score = sum(rewards) / len(rewards) if rewards else 0.0
    success = score > 0.5

    log_end(success, step_count, score, rewards)

if __name__ == "__main__":
    run_episode("easy")
