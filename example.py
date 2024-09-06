from WYK.Judge import Judge

if __name__ == "__main__":
    llm_name = "unsloth/mistral-7b-instruct-v0.3-bnb-4bit"
    judge = Judge(
        red_agent_model=llm_name,
        blue_agent_model=llm_name,
        judge_model=llm_name,
        debug=True,
    )
    print(f"LLM '{llm_name}' scored {judge.assess()[0]}")
