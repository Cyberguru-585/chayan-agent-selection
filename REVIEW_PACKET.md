# REVIEW PACKET

## 1. Entry Point
main.py

## 2. Core Execution Flow
main.py → agent_selector.py → rules.py

## 3. Input → Output Example

Input:
{
  "actor": "intent-router",
  "action": "task.process",
  "context": {
    "task": "summarize-and-format"
  }
}

Output:
{
  "actor": "intent-router",
  "action": "task.process",
  "agents": ["1", "2"],
  "sequence": ["1", "2"],
  "context": {
    "task": "summarize-and-format"
  }
}

## 4. What was built
- Deterministic agent selection engine
- Rule-based task mapping
- Structured output contract
- Failure handling for invalid tasks

## 5. Failure Cases
- Unknown task → returns structured failure

## 6. Proof
Run test_cases.py to view outputs in console