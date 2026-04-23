from agent_selector import select_agents


if __name__ == "__main__":
    input_data = {
        "actor": "intent-router",
        "action": "task.process",
        "context": {
            "task": "summarize-and-format"
        }
    }

    output = select_agents(input_data)
    print("OUTPUT:\n", output)