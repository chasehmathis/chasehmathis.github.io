"""Silicon-sampling income experiment via the Anthropic API.

US individual income is right-skewed, so mean >> median >> mode.
If the LLM is collapsing to the *mean*, answers cluster around ~$60k+.
If collapsing to the *median*, around ~$40k.
If to the *mode*, lower still.

Usage:
    export ANTHROPIC_API_KEY=...
    python income_experiment_api.py [N] [out.csv]
"""
import csv
import random
import sys

import anthropic

N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
OUT = sys.argv[2] if len(sys.argv) > 2 else "results_income_api.csv"
MODEL = "claude-opus-4-7"
TEMPERATURE = 1.0

client = anthropic.Anthropic()


def ask(sex: str, age: int) -> str:
    msg = client.messages.create(
        model=MODEL,
        max_tokens=15,
        temperature=TEMPERATURE,
        messages=[
            {
                "role": "user",
                "content": (
                    f"You are a {age}-year-old {sex} American sampled at random "
                    f"from the working-age population. What is your annual "
                    f"personal income in US dollars? Respond with only a single "
                    f"number, no commas, no dollar sign, no words."
                ),
            }
        ],
    )
    return msg.content[0].text.strip()


def main() -> None:
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["run", "sex", "age", "income_usd"])
        for i in range(1, N + 1):
            sex = random.choice(["male", "female"])
            age = random.randint(22, 64)
            try:
                ans = ask(sex, age)
            except Exception as e:
                ans = f"ERROR:{e.__class__.__name__}"
            w.writerow([i, sex, age, ans])
            f.flush()
            print(f"run {i}: {sex} age {age} -> {ans}")


if __name__ == "__main__":
    main()
