---
license: mit
task_categories:
  - text-classification
language:
  - en
tags:
  - prompt-injection
  - security
  - llm
  - ai-safety
pretty_name: Prompt Injection Benchmark
size_categories:
  - n<1K
---

# Prompt Injection Benchmark

A curated dataset of labeled prompt injection attacks and benign prompts for testing and benchmarking injection detection systems.

## Dataset Description

This dataset contains 200 examples across 7 attack categories, plus 100 benign prompts. Each example is labeled with:
- `text`: The prompt text
- `label`: `injection` or `benign`
- `category`: Attack category (e.g., `instruction_override`, `role_hijack`)
- `severity`: `low`, `medium`, `high`, or `critical`

## Attack Categories

| Category | Count | Description |
|---|---|---|
| instruction_override | 30 | "Ignore previous instructions" variants |
| role_hijack | 30 | "You are now..." identity takeover |
| system_prompt_leak | 25 | Attempts to extract system prompts |
| delimiter_injection | 25 | Fake system/assistant markers |
| encoding_bypass | 20 | Base64, Unicode trick attacks |
| jailbreak | 35 | DAN, safety bypass attempts |
| data_exfiltration | 35 | Extract data or make external requests |
| benign | 100 | Normal, safe prompts |

## Usage

```python
from datasets import load_dataset
ds = load_dataset("zachz/prompt-injection-benchmark")
```

## Use Cases

- Benchmark prompt injection detectors
- Train classifiers for injection detection
- Red-team testing for LLM applications
- Security auditing of AI systems

## License

MIT
