---
license: apache-2.0
ask_categories:
- text-classification
- text-generation
tags:
- safety
- alignment
- red-teaming
- prompt-injection
- jailbreak
- obfuscation
- synthetic
- evaluation
pretty_name: Prompt Injection (Synthetic) — GPT-OSS-120b
dataset_type: text
---

# Prompt Injection (Synthetic) — GPT-OSS-120b

This dataset contains a small collection of **synthetic user prompts** and **Noraml user prompts** designed to finetune Large Language Models (LLMs) against **malicious prompt-injection / jailbreak attempts**, including cases that use **obfuscation** (e.g., Base64, leetspeak, typos, irregular spacing) to evade safety filters.

## Dataset Summary

- **Source repository:** `Lilbullet/prompt-injection-artificial-GPTOSS120b`
- **Model used:** GPT-OSS-120b
- **Generation date:** 2026-02-06
- **Format:** JSON
- **Total samples:** 4000

## Intended Use

This dataset is intended for:
- Safety evaluation and red-teaming of LLMs
- Benchmarking and training *classifiers* for malicious intent / prompt injection detection
- Measuring robustness to common obfuscation strategies

## Data Schema

Each record follows the schema below:

| Field | Type | Description |
|---|---|---|
| `text` | string | Raw user prompt containing malicious intent (may be obfuscated) |
| `label` | string | Primary classification label (e.g., `malicious`) |
| `subtype` | string | Attack subtype (e.g., `obfuscated`) |
| `rationale` | string | One-sentence explanation of why the prompt is considered malicious |

### Example (sanitized)

```json
{
  "text": "<obfuscated malicious request omitted>",
  "label": "malicious",
  "subtype": "obfuscated",
  "rationale": "The prompt disguises disallowed intent using obfuscation to evade safeguards."
}
---
