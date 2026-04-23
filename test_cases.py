from agent_selector import select_agents


test_inputs = [
    {"task": "summarize-and-format"},
    {"task": "translate-and-summarize"},
    {"task": "format-only"},
    {"task": "translate-only"},
    {"task": "invalid-task"}
]


for i, test in enumerate(test_inputs, 1):
    input_data = {
        "actor": "intent-router",
        "action": "task.process",
        "context": test
    }

    print(f"\nTest Case {i}: {test['task']}")
    print(select_agents(input_data))