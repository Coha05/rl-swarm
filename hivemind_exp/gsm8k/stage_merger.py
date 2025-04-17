from typing import Any


def merge_stage1_question(outputs: dict[str, dict[str, Any]]):
    merged = {"question": None, "answer": None, "agent_answers": {}}
    for agent, o in outputs.items():
        if not all(k in o for k in ("question", "answer", "agent_answers")):
            print(f"[Warning] Skipped malformed stage1 output from {agent}: {o}")
            continue
        merged["question"] = o["question"]
        merged["answer"] = o["answer"]
        merged["agent_answers"].update(o["agent_answers"])
    for agent in outputs:
        if agent not in merged["agent_answers"]:
            merged["agent_answers"][agent] = "No answer received..."
    return merged

def merge_stage2_question(outputs: dict[str, dict[str, Any]]):
    merged = {
        "question": None,
        "answer": None,
        "stage2_prompt": None,
        "agent_opinion": {},
    }
    for agent, o in outputs.items():
        if not isinstance(o, dict):
            print(f"[Warning] Skipped malformed stage2 output from {agent}: {o}")
            continue
        for col in ["question", "answer", "stage2_prompt"]:
            if col in o:
                merged[col] = o[col]
        if "agent_opinion" in o:
            merged["agent_opinion"].update(o["agent_opinion"])
    for agent in outputs:
        if agent not in merged["agent_opinion"]:
            merged["agent_opinion"][agent] = "No feedback received..."
    return merged
