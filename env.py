from models import Observation, Action
from tasks import TASKS

class MiniSOCEnv:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        self.tasks = TASKS[difficulty]
        self.current_index = 0
        self.done = False

    def reset(self):
        self.current_index = 0
        self.done = False
        task = self.tasks[self.current_index]

        return Observation(
            log=task["log"],
            context=task["context"]
        )

    def step(self, action: Action):
        if self.done:
            return None, 0.0, True, {}

        task = self.tasks[self.current_index]
        correct = task["answer"]

        # 🔥 ADVANCED REWARD
        if action.decision == correct:
            reward = 1.0 * action.confidence
        elif action.decision == "flag" and correct == "escalate":
            reward = 0.5 * action.confidence
        else:
            reward = -0.2 * action.confidence  # penalty

        self.current_index += 1

        if self.current_index >= len(self.tasks):
            self.done = True
            return None, reward, True, {}

        next_task = self.tasks[self.current_index]

        return Observation(
            log=next_task["log"],
            context=next_task["context"]
        ), reward, False, {}

    def state(self):
        return {
            "difficulty": self.difficulty,
            "step": self.current_index,
            "done": self.done
        }