from fastapi import FastAPI
from models import Action
from env import MiniSOCEnv

app = FastAPI()

envs = {
    "easy": MiniSOCEnv("easy"),
    "medium": MiniSOCEnv("medium"),
    "hard": MiniSOCEnv("hard"),
}

current_env = envs["easy"]

@app.get("/")
def root():
    return {"message": "Mini SOC Environment Running 🚀"}


# 🔥 FIX: SUPPORT BOTH GET + POST
@app.get("/reset")
@app.post("/reset")
def reset(level: str = "easy"):
    global current_env
    current_env = envs[level]
    return current_env.reset()


@app.post("/step")
def step(action: Action):
    observation, reward, done, info = current_env.step(action)
    return {
        "observation": observation,
        "reward": reward,
        "done": done,
        "info": info
    }


@app.get("/state")
def state():
    return current_env.state()