from WYK.Judge import Judge
from pprint import pprint

if __name__ == "__main__":
    LLMS = [
        "unsloth/mistral-7b-instruct-v0.3-bnb-4bit",
        "unsloth/Phi-3-mini-4k-instruct-bnb-4bit",
        "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit",
    ]

    scores = []
    for red_llm in LLMS:
        for blue_llm in LLMS:

            judge = Judge(
                red_agent_model=red_llm,
                blue_agent_model=blue_llm,
                judge_model="unsloth/mistral-7b-instruct-v0.3-bnb-4bit",
                debug=True,
            )

            score, rational, list_of_responses = judge.assess()

            scores.append(
                {
                    "red": red_llm,
                    "blue": blue_llm,
                    "score": score,
                    "conversation": list_of_responses,
                }
            )

    pprint(scores)