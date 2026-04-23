from rules import TASK_AGENT_MAP


def select_agents(input_data):
    try:
        task = input_data["context"]["task"]

        if task not in TASK_AGENT_MAP:
            return {
                "failure": {
                    "code": "UNKNOWN_TASK",
                    "message": "No matching task found"
                }
            }

        agents = TASK_AGENT_MAP[task]

        return {
            "actor": input_data["actor"],
            "action": input_data["action"],
            "agents": agents,
            "sequence": agents, 
            "context": input_data["context"]
        }

    except Exception as e:
        return {
            "failure": {
                "code": "INVALID_INPUT",
                "message": str(e)
            }
        }
