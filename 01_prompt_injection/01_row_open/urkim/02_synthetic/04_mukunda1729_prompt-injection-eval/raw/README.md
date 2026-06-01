---
license: mit
task_categories:
- text-classification
language:
- en
tags:
- llm
- rag
- security
- prompt-injection
- guardrails
- evaluation
size_categories:
- n<1K
configs:
- config_name: default
  data_files: data.csv
---

# Prompt Injection Eval Set

A small, hand-written evaluation set for testing prompt-injection detectors and RAG guardrails. Built as a companion to the [prompt-injection-shield](https://github.com/MukundaKatta/prompt-injection-shield) library.

## Why

Most prompt-injection corpora target *training* (thousands of synthetic rows). This one targets *evaluation*: every row is hand-curated, labeled with a category and severity, and short enough to debug by eye when a detector misfires.

## Schema

| field | type | description |
| --- | --- | --- |
| `text` | string | The candidate passage |
| `label` | string | `clean`, `injection`, or `borderline` |
| `category` | string | Sub-type (see below) |
| `severity` | string | `none`, `low`, `medium`, `high`, `critical` |
| `source` | string | Provenance tag |

## Categories

- `benign` — clean reference text
- `classic_override` — "ignore previous instructions" family
- `url_exfiltration` — instructs the model to call out to an attacker URL
- `system_impersonation` — fakes a `[SYSTEM]` / `<|system|>` block
- `tool_hijack` — tries to redirect tool calls (delete, transfer, exec)
- `role_override` — persona swap to remove guardrails
- `encoded_obfuscation` — base64 / rot13 / acrostic payloads
- `indirect_rag_poison` — payload hidden inside otherwise-benign retrieved content
- `discussed_not_executed` — borderline rows that *describe* injections without performing them (good for false-positive checks)

## Distribution

- 74 rows total
- 20 clean / 50 injection / 4 borderline
- All entries are synthetic and original to this dataset

## Quickstart

```python
from datasets import load_dataset
ds = load_dataset("mukunda1729/prompt-injection-eval", split="train")
print(ds[0])
```

Or pair it directly with the detector:

```python
from datasets import load_dataset
from prompt_injection_shield import scan

ds = load_dataset("mukunda1729/prompt-injection-eval", split="train")
hits = sum(1 for row in ds if row["label"] == "injection" and scan(row["text"]).flagged)
print(f"recall on injections: {hits} / {sum(1 for r in ds if r['label']=='injection')}")
```

## License

MIT.

## Related

- [prompt-injection-shield](https://github.com/MukundaKatta/prompt-injection-shield) — the detector this was built against
- [prompt-injection-shield-demo](https://huggingface.co/spaces/mukunda1729/prompt-injection-shield-demo) — live Streamlit demo
- [rag-guardrails-action](https://github.com/MukundaKatta/rag-guardrails-action) — GitHub Action that runs the detector in CI
